from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] or grid[-1][-1]: return -1
        n, stack, c = len(grid), [(0,0)], 0
        while stack:
            c += 1
            for _ in range(len(stack)):
                cell = stack.pop(0)
                if cell[0] == n-1 and cell[1] == n-1:
                    return c
                for i, j in ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)):
                    x, y = cell[0] + i, cell[1] + j
                    if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                        grid[x][y] = 1
                        stack.append((x,y))
        return -1
