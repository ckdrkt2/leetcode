from typing import List
class union_find:
    def __init__(self, n):
        self.p = [i for i in range(n)]

    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x1, x2):
        p1 = self.find(x1)
        p2 = self.find(x2)
        if p1 == p2: return
        self.p[p2] = p1

class Solution:
    def neigh(self, row, col, rows, cols):
        n = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]
        return [e for e in n if e[0] >= 0 and e[0] < rows and e[1] >= 0 and e[1] < cols]

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        rows, cols = row, col
        cells = [[c[0] - 1, c[1] - 1] for c in cells]
        grid = [[1 for _ in range(cols)] for _ in range(rows)]
        uf = union_find(rows * cols + 2)

        def index(x, y):
            return x * cols + y + 1

        for i in range(len(cells) - 1, -1, -1):
            grid[cells[i][0]][cells[i][1]] = 0
            for x in self.neigh(cells[i][0], cells[i][1], rows, cols):
                if grid[x[0]][x[1]] == 1: continue
                uf.union(index(cells[i][0], cells[i][1]), index(x[0], x[1]))
            if cells[i][0] == 0:
                uf.union(index(cells[i][0], cells[i][1]), 0)
            if cells[i][0] == rows - 1:
                uf.union(index(cells[i][0], cells[i][1]), rows * cols + 1)
            if uf.find(0) == uf.find(rows * cols + 1):
                return i