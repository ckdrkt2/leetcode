from typing import List
from math import ceil
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) >= hour + 1: return -1

        lo, hi = 1, 1000000000

        while lo < hi:
            m = (lo + hi) // 2
            res = sum([ceil(i / m) for i in dist[:-1]]) + (dist[-1] / m)
            if res <= hour:
                hi = m
            else:
                lo = m + 1
        return lo
