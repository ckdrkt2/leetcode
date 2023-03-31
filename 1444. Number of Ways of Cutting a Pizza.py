from typing import List
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m, n = len(pizza), len(pizza[0])
        acnt = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                acnt[i][j] = int(pizza[i][j] == 'A') + acnt[i + 1][j] + acnt[i][j + 1] - acnt[i + 1][j + 1]
        dp = [[int(acnt[i][j] > 0) for j in range(n)] for i in range(m)]
        for _ in range(1, k):
            for i in range(m):
                for j in range(n):
                    val = 0
                    for c in range(i + 1, m):
                        val += dp[c][j] if acnt[i][j] > acnt[c][j] else 0
                    for c in range(j + 1, n):
                        val += dp[i][c] if acnt[i][j] > acnt[i][c] else 0
                    dp[i][j] = val % 1000000007
        return dp[0][0]
