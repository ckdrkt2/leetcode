class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        idx = bisect_left(nums, target)
        if idx >= len(nums) or nums[idx] != target: return [-1, -1]
        return [idx, bisect_right(nums, target) - 1]
