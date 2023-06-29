# NOT MY SOLUTION
from typing import List
from itertools import product
from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        keys, start = 0, None
        for i, j in product(range(len(grid)), range(len(grid[0]))):
            if 'a' <= grid[i][j] <= 'f':
                keys += 1
            elif grid[i][j] == '@':
                start = (i, j)
        queue = deque([(start, 0, 0)])
        seen = {(start, 0)}
        while queue:
            (x, y), steps, obtained = queue.popleft()
            if grid[x][y] == '#' or (grid[x][y].isupper() and not (obtained & (1 << (ord(grid[x][y].lower()) - ord('a'))))): continue
            if 'a' <= grid[x][y] <= 'f':
                obtained |= 1 << (ord(grid[x][y]) - ord('a'))
                if obtained == (1 << keys) - 1: return steps
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and ((nx, ny), obtained) not in seen:
                    seen.add(((nx, ny), obtained))
                    queue.append(((nx, ny), steps + 1, obtained))
        return -1
