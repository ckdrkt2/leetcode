class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        n = n * (n+1) // 2
        for i in nums:
            n -= i
        return n