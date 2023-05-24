from heapq import heappush, heappop
from typing import List
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        total = ans = 0
        heap = []

        for pair in sorted(zip(nums1, nums2), key=lambda x: -x[1]):
            num1, num2 = pair
            heappush(heap, num1)
            total += num1
            if len(heap) > k: total -= heappop(heap)
            if len(heap) == k: ans = max(ans, total * num2)
        return ans
