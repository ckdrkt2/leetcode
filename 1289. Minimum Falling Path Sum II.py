from typing import List

class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        dp, n = grid[0], len(grid)

        for i in range(1, n):
            idx1 = dp.index(min(dp))
            idx2 = dp.index(min(dp[:idx1] + dp[idx1 + 1:]))
            for j in range(n):
                if j != idx1:
                    grid[i][j] += dp[idx1]
                else:
                    grid[i][j] += dp[idx2]
            dp = grid[i]

        return min(dp)
