from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        def bfs(lst):
            q = deque(lst)
            while q:
                (i, j) = q.popleft()
                for (di, dj) in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= di+i < m and 0 <= dj+j < n and (di+i, dj+j) not in lst \
                        and heights[di+i][dj+j] >= heights[i][j]:
                        q.append( (di+i,dj+j) )
                        lst.add( (di+i, dj+j) )
            return lst
        pacific = set ([(i, 0) for i in range(m)] + [(0, j) for j in range(1, n)])
        atlantic = set ([(i, n-1) for i in range(m)] + [(m-1, j) for j in range(n-1)])
        return list(bfs(pacific) & bfs(atlantic))