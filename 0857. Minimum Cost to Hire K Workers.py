from typing import List
from heapq import heapify, heapreplace

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pairs = sorted(zip(quality, wage), key=lambda p: p[1] / p[0])
        h = [-q for q, _ in pairs[:k]]
        heapify(h)
        sum_q = -sum(h)
        ans = sum_q * pairs[k-1][1] / pairs[k-1][0]
        for q, w in pairs[k:]:
            if q < -h[0]:
                sum_q += heapreplace(h, -q) + q
                ans = min(ans, sum_q * w / q)
        return ans
