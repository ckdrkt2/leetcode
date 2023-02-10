from typing import List
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = []
        count, n = 0, len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    count += 1
                    q.append((i,j,0))
        if not q or count == n * n: return -1
        for i, j, d in q:
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < n and 0 <= y < n and grid[x][y] != 1:
                    grid[x][y] = 1
                    q.append((x, y, d + 1))
        return q[-1][-1]