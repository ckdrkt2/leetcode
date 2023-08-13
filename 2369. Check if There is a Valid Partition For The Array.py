from typing import List
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [True, False, nums[0] == nums[1]]
        for i in range(2, len(nums)):
            cur = False
            if nums[i] == nums[i - 1] and dp[1]:
                cur = True
            elif nums[i] == nums[i - 1] == nums[i - 2] and dp[0]:
                cur = True
            elif nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2] == 1 and dp[0]:
                cur = True
            dp[0], dp[1], dp[2] = dp[1], dp[2], cur
        return dp[2]
