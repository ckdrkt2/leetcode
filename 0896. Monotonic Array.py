from typing import List
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        pattern = nums[len(nums) - 1] > nums[0]
        return all((nums[i] > nums[i-1]) == pattern or nums[i] == nums[i-1] for i in range(1, len(nums)))
