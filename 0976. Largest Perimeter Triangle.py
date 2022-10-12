class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        b, a = nums[0], nums[1]
        for i in range(2, len(nums)):
            c, b, a = b, a, nums[i]
            if c < a + b: return a + b + c
        return 0