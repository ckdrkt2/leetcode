from typing import List
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n, ans = len(grid), len(grid[0]), 0
        def dfs(row, col):
            is_island = True
            grid[row][col] = 1
            if row == 0 or col == 0 or row == m - 1 or col == n - 1:
                is_island = False
            if row > 0 and grid[row - 1][col] == 0:
                is_island = dfs(row - 1, col) and is_island
            if col > 0 and grid[row][col - 1] == 0:
                is_island = dfs(row, col - 1) and is_island
            if row < m - 1 and grid[row + 1][col] == 0:
                is_island = dfs(row + 1, col) and is_island
            if col < n - 1 and grid[row][col + 1] == 0:
                is_island = dfs(row, col + 1) and is_island
            return is_island

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and dfs(i, j): ans += 1
        return ans
