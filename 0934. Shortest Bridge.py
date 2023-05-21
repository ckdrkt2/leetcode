from typing import List
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def distance(p1, p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) - 1

        n, i = len(grid), 0
        visited, borders = set(), [set(), set()]

        def dfs(r, c):
            for nR, nC in (r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c):
                if 0 <= nR < n and 0 <= nC < n and not grid[nR][nC]:
                    borders[i].add((r, c))
                    break
            visited.add((r, c))
            for nR, nC in (r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c):
                if 0 <= nR < n and 0 <= nC < n and grid[nR][nC] and (nR, nC) not in visited:
                    dfs(nR, nC)

        for row in range(n):
            if i == 2: break
            for col in range(n):
                if (row, col) not in visited and grid[row][col]:
                    dfs(row, col)
                    i += 1
                    if i == 2: break

        minDistance = 101
        for i1 in borders[0]:
            for i2 in borders[1]:
                minDistance = min(minDistance, distance(i1, i2))
                if minDistance == 1:
                    return 1

        return minDistance


