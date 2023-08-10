from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            m = (lo + hi) // 2
            if nums[m] == target: return True
            if nums[m] < nums[hi]:
                if nums[m] < target <= nums[hi]:
                    lo = m + 1
                else:
                    hi = m - 1
            elif nums[m] > nums[hi]:
                if nums[lo] <= target < nums[m]:
                    hi = m - 1
                else:
                    lo = m + 1
            else:
                hi -= 1
        return False
