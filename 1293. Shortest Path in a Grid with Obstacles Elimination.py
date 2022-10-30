from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        stack = deque([(0, 0, 0)])
        visited = {(0, 0): 0}
        steps = 0
        while stack:
            for _ in range(len(stack)):
                r, c, obs = stack.popleft()
                if obs > k: continue
                if r == m - 1 and c == n - 1: return steps
                for r2, c2 in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                    if not (0 <= r2 < m and 0 <= c2 < n): continue
                    next_obs = obs + grid[r2][c2]
                    if next_obs < visited.get((r2, c2), float('inf')):
                        visited[(r2, c2)] = next_obs
                        stack.append([r2, c2, next_obs])
            steps += 1
        return -1