from typing import List
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        ans, nums = 0, sorted(nums)
        for i in range(len(nums) // 2):
            ans = max(ans, nums[i] + nums[-(i + 1)])
        return ans
