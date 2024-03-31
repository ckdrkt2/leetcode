from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        isMin = isMax = isnot = -1
        for i, num in enumerate(nums):
            if not minK <= num <= maxK: isnot = i
            if num == minK: isMin = i
            if num == maxK: isMax = i
            ans += max(0, min(isMin, isMax) - isnot)
        return ans
