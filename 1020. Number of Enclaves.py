from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            grid[i][j] = 0
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if not (0 <= x < m or 0 <= y < n): continue
                if grid[x][y] == 1: dfs(x, y)
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == 1: dfs(i, j)
        return sum(sum(row) for row in grid)
