from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        groups = []
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1 and (i == 0 or land[i - 1][j] == 0) and (j == 0 or land[i][j - 1] == 0):
                    r2, c2 = i, j
                    while r2 + 1 < m and land[r2 + 1][c2] == 1:
                        r2 += 1
                    while c2 + 1 < n and land[r2][c2 + 1] == 1:
                        c2 += 1
                    groups.append([i, j, r2, c2])
        return groups
