from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, prev):
            for nei in graph[node]:
                if nei != prev and dfs(nei, node):
                    hasApple[node] = True
            return hasApple[node]

        dfs(0, -1)
        return (sum(hasApple) - hasApple[0]) * 2