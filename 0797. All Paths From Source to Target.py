from collections import deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans, q = [], deque([[0]])
        while q:
            cur = q.popleft()
            if cur[-1] == len(graph):
                ans.append(cur)
            else:
                for i in graph[cur[-1]]:
                    q.append(cur + [i])
        return ans