from typing import List
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [0] * (len(s) + 1)
        for i in range(1, len(s) + 1):
            m = float('inf')
            for k in range(i):
                if s[k:i] in dictionary:
                    m = min(dp[k], m)
                else:
                    m = min(dp[k]+i-k, m)
            dp[i] = m
        return dp[-1]
