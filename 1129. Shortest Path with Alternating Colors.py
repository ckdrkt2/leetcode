from typing import List
from collections import defaultdict, deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in redEdges: graph[a].append((b, "r"))
        for u, v in blueEdges: graph[u].append((v, "b"))
        ans = [-1] * n
        queue, visited = deque([(0, 0, None)]), set()
        while queue:
            node, dist, prev = queue.popleft()
            visited.add((node, prev))
            if ans[node] == -1: ans[node] = dist
            else: ans[node] = min(ans[node], dist)
            for neighbor, edge in graph[node]:
                if (neighbor, edge) not in visited and prev != edge:
                    queue.append((neighbor, dist + 1, edge))
        return ans