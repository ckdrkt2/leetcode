from typing import List
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = nums[:]
        for diff in range(1, len(nums)):
            for left in range(len(nums) - diff):
                right = left + diff
                dp[left] = max(nums[left] - dp[left + 1], nums[right] - dp[left])
        return dp[0] >= 0
