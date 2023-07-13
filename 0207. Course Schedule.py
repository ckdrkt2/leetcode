from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        for prerequisite in prerequisites:
            adj[prerequisite[1]].append(prerequisite[0])

        seen = [False] * numCourses
        inStack = [False] * numCourses
        for i in range(numCourses):
            if self.dfs(i, adj, seen, inStack):
                return False
        return True

    def dfs(self, node, adj, seen, inStack):
        if inStack[node]: return True
        if seen[node]: return False

        seen[node] = True
        inStack[node] = True
        for neighbor in adj[node]:
            if self.dfs(neighbor, adj, seen, inStack):
                return True
        inStack[node] = False
        return False
