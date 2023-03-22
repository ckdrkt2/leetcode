from collections import deque, defaultdict
from typing import List
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for u, v, w in roads:
            graph[u][v] = graph[v][u] = w

        ans, seen = 1000000, set()
        q = deque([1])

        while q:
            node = q.popleft()
            for adj, scr in graph[node].items():
                if adj not in seen:
                    q.append(adj)
                    seen.add(adj)
                ans = min(ans, scr)
        return ans
