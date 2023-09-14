from typing import List
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for [src, dest] in tickets:
            graph[src].append(dest)
        for src in graph:
            graph[src].sort(reverse=True)

        stack, ans = ['JFK'], []

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            ans.append(stack.pop())

        return ans[::-1]
