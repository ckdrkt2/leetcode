class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] *= nums[i]j 
        return sorted(nums)