class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def island(i, j):
            if grid[i][j] == '0': return 0
            grid[i][j] = '0'
            if i > 0: island(i-1, j)
            if i < m-1 : island(i+1, j)
            if j > 0: island(i, j-1)
            if j < n-1: island(i, j+1)
            return 1
        m, n, ans = len(grid), len(grid[0]), 0
        for i, g in enumerate(grid):
            for j, _ in enumerate(g):
                ans += island(i,j)
        return ans