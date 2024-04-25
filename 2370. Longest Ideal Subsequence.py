from string import ascii_lowercase

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp, ans = [0] * 26, 1

        for c in s:
            i = ascii_lowercase.find(c)
            dp[i] = 1 + max(dp[i], max(dp[max(0, i - k): i] + dp[i + 1: k + i + 1] + [0]))
            ans = max(ans, dp[i])

        return ans
