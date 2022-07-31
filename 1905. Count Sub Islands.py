class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i, j):
            res, cur = [], False
            if grid2[i][j]:
                grid2[i][j] = 0
                if i > 0 and grid2[i - 1][j]: res.append(dfs(i - 1, j))
                if i < m - 1 and grid2[i + 1][j]: res.append(dfs(i + 1, j))
                if j > 0 and grid2[i][j - 1]: res.append(dfs(i, j - 1))
                if j < n - 1 and grid2[i][j + 1]: res.append(dfs(i, j + 1))
                if grid1[i][j]: cur = True
            if not res: res.append(1)
            return cur and (sum(res) == len(res))

        m, n = len(grid1), len(grid1[0])
        return sum(dfs(i, j) for i in range(m) for j in range(n))
