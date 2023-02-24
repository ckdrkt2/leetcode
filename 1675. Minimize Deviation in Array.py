from typing import List
from heapq import heappush, heappop
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap, ans = [], float('inf')
        for n in nums: heappush(heap, -n * 2 if n % 2 else -n)
        m = -max(heap)
        while len(heap) == len(nums):
            n = -heappop(heap)
            ans = min(ans, n - m)
            if n % 2 == 0:
                m = min(m, n // 2)
                heappush(heap, -n // 2)
        return ans