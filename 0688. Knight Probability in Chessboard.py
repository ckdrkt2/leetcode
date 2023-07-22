class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        diffs = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

        dp = [[[0] * (k+1) for c in range(n)] for r in range(n)]
        dp[row][column][0] = 1

        for m in range(1, k+1):
            for r in range(n):
                for c in range(n):
                    dp[r][c][m] = 0.125 * sum(dp[r+x][c+y][m-1] for x, y in diffs if 0 <= r+x < n and 0 <= c+y < n)
        return sum(dp[r][c][k] for r in range(n) for c in range(n))
