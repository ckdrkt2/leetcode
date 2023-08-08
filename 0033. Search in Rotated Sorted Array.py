from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            m = (lo + hi) // 2
            if nums[m] == target: return m
            if nums[lo] <= nums[m]:
                if nums[lo] <= target <= nums[m]:
                    hi = m - 1
                else:
                    lo = m + 1
            else:
                if nums[m] < target <= nums[hi]:
                    lo = m + 1
                else:
                    hi = m - 1
        return -1
