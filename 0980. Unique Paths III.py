class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n, empty = len(grid), len(grid[0]), 1
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1: x, y = i, j
                elif grid[i][j]==0: empty += 1
        self.ans = 0
        def dfs(x, y, empty):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] < 0: return
            if grid[x][y]==2:
                self.ans += empty == 0
                return
            grid[x][y] = -2
            dfs(x + 1, y, empty - 1)
            dfs(x - 1, y, empty - 1)
            dfs(x, y + 1, empty - 1)
            dfs(x, y - 1, empty - 1)
            grid[x][y] = 0
        dfs(x, y, empty)
        return self.ans