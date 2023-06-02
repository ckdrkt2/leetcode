from typing import List
from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph, n = defaultdict(list), len(bombs)
        for i in range(n):
            for j in range(n):
                if i == j: continue
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]

                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)

        def dfs(cur, seen):
            seen.add(cur)
            for neib in graph[cur]:
                if neib not in seen:
                    dfs(neib, seen)
            return len(seen)

        ans = 0
        for i in range(n):
            visited = set()
            ans = max(ans, dfs(i, visited))
        return ans
