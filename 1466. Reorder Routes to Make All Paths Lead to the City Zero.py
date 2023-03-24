from typing import List
from collections import deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        inEdges = [[] for _ in range(n)]
        outEdges = [[] for _ in range(n)]
        for (u, v) in connections:
            inEdges[v].append(u)
            outEdges[u].append(v)

        seen, ans, q = set(), 0, deque([0])
        while q:
            node = q.popleft()
            seen.add(node)
            for nei in inEdges[node]:
                if nei not in seen:
                    q.append(nei)
            for nei in outEdges[node]:
                if nei not in seen:
                    q.append(nei)
                    ans += 1
        return ans
