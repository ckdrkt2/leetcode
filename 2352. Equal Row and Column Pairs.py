from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans, n = 0, len(grid)
        row, col = [[] for _ in range(n)], [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                num = grid[i][j]
                row[i].append(num)
                col[j].append(num)
        return sum([row[i] == col[j] for i in range(n) for j in range(n)])
