class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + [0] * high
        for i in range(1, high + 1):
            dp[i] = (dp[i - zero] + dp[i - one])
        return sum(dp[i] for i in range(low, high + 1)) % 1000000007
