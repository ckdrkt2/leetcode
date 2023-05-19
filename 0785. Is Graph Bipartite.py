from typing import List
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n, colored = len(graph), {}
        def dfs(color, idx, graph, colored):
            if idx in colored: return color == colored[idx]
            colored[idx] = color                            
            return all(dfs(-color, nb, graph, colored) for nb in graph[idx])
        return all(i in colored or dfs(1, i, graph, colored) for i in range(n))
