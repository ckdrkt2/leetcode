class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:

        def dfs(i: int, j: int) -> int:
            d, tmp, grid[i][j] = [0], grid[i][j], 0
            if i != 0 and grid[i - 1][j]: d.append(dfs(i - 1, j))
            if i != m - 1 and grid[i + 1][j]: d.append(dfs(i + 1, j))
            if j != 0 and grid[i][j - 1]: d.append(dfs(i, j - 1))
            if j != n - 1 and grid[i][j + 1]: d.append(dfs(i, j + 1))
            grid[i][j] = tmp
            return tmp + max(d)

        m, n, ans = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    ans = max(ans, dfs(i, j))
        return ans
