from typing import List
from string import ascii_lowercase
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        al = {c: i for i, c in enumerate(ascii_lowercase)}
        m, n = len(target), len(words[0])
        cnt = [[0] * n for _ in range(26)]
        dp = [[-1] * (n + 1) for _ in range(m + 1)]

        for j in range(n):
            for word in words:
                cnt[al[word[j]]][j] += 1

        def f(i, j):
            if j == 0: return 0 if i else 1
            if dp[i][j] != -1: return dp[i][j]
            dp[i][j] = f(i, j - 1)
            if i: dp[i][j] += (cnt[al[target[i - 1]]][j - 1] * f(i - 1, j - 1))
            dp[i][j] %= 1000000007
            return dp[i][j]

        return f(m, n)
