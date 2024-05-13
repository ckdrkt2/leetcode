from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n, ans = len(grid), len(grid[0]), 0
        for i in range(m):
            if grid[i][0] == 0:
                grid[i] = [1 - x for x in grid[i]]

        for i, col in enumerate(zip(*grid)):
            cnt = sum(col)
            ans += 2 ** (n - i - 1) * max(cnt, m - cnt)

        return ans
