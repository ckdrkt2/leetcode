class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        a = [-1] * n
        for start in range(n):
            j = start
            for i in range(m):
                g = grid[i][j]
                j += g
                if 0 <= j < n:
                    if g != grid[i][j]:
                        break
                    if i == m-1: a[start] = j
                else: break
        return a