from heapq import heappop, heappush
class Solution(object):
    def minimumEffortPath(self, heights):
        m, n = len(heights), len(heights[0])
        dist = [[1000001] * n for _ in range(m)]
        heap, direct = [(0, 0, 0)], ((0,1),(1,0),(0,-1),(-1,0))
        while heap:
            d, r, c = heappop(heap)
            if d > dist[r][c]: continue
            if r == m - 1 and c == n - 1: break
            for i, j in direct:
                nr, nc = r + i, c + j
                if 0 <= nr < m and 0 <= nc < n:
                    new = max(d, abs(heights[nr][nc] - heights[r][c]))
                    if dist[nr][nc] > new:
                        dist[nr][nc] = new
                        heappush(heap, (dist[nr][nc], nr, nc))
        return d
