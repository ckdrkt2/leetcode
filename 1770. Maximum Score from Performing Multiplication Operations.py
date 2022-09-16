class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0] * (m+1) for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(m-i- 1, -1, -1):
                mm = multipliers[i+j]
                dp[i][j] = max(mm*nums[i] + dp[i+1][j], mm*nums[n-j-1] + dp[i][j+1])
        return dp[0][0]