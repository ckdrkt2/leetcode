class Solution:
    def findPaths(self, m: int, n: int, N: int, x: int, y: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[x][y], ans = 1, 0

        for moves in range(1, N + 1):
            temp = [[0] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    if i == m - 1:
                        ans = (ans + dp[i][j]) % 1000000007
                    if j == n - 1:
                        ans = (ans + dp[i][j]) % 1000000007
                    if i == 0:
                        ans = (ans + dp[i][j]) % 1000000007
                    if j == 0:
                        ans = (ans + dp[i][j]) % 1000000007
                    temp[i][j] = (
                        ((dp[i - 1][j] if i > 0 else 0) + (dp[i + 1][j] if i < m - 1 else 0)) +
                        ((dp[i][j - 1] if j > 0 else 0) + (dp[i][j + 1] if j < n - 1 else 0))
                    ) % 1000000007

            dp = temp

        return ans
