from typing import List
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        isSafe = [1 if len(node) == 0 else -1 for node in graph]

        for i in range(len(graph)):
            isSafe[i] = self.dfs(graph, i, isSafe)

        return [i for i in range(len(graph)) if isSafe[i] == 1]

    def dfs(self, graph, node, isSafe):
        for nei in graph[node]:
            if isSafe[nei] == -1:
                isSafe[nei] = 0
                isSafe[nei] = self.dfs(graph, nei, isSafe)

            if isSafe[nei] == 0: return 0
        return 1
