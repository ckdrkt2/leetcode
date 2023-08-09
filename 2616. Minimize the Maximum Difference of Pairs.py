from typing import List
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:
            m = (lo + hi) // 2
            k, i = 0, 1
            while i < len(nums):
                if nums[i] - nums[i - 1] <= m:
                    k += 1
                    i += 1
                i += 1
            if k >= p:
                hi = m
            else:
                lo = m + 1
        return lo
