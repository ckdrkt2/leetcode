from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0] + [10000 for _ in range(len(nums) - 1)]
        for i, n in enumerate(nums):
            cnt = dp[i]
            for j in range(i + 1, min(len(nums), i + n + 1)):
                dp[j] = min(dp[j], cnt + 1)
        return dp[-1]