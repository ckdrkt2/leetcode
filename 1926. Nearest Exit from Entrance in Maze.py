from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
        maze[entrance[0]][entrance[1]] = '+'

        queue = deque([(entrance[0], entrance[1], 0)])
        while queue:
            x, y, dist = queue.popleft()
            for xi, yi in dirs:
                nx = x + xi
                ny = y + yi

                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    if 0 == nx or nx == m - 1 or 0 == ny or ny == n - 1:
                        return dist + 1
                    maze[nx][ny] = '+'
                    queue.append([nx, ny, dist + 1])
        return -1