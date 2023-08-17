from typing import List
from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        ans = 0
        adj = defaultdict(set)
        for road in roads:
            adj[road[0]].add(road[1])
            adj[road[1]].add(road[0])

        for node1 in range(n):
            for node2 in range(node1 + 1, n):
                cur = len(adj[node1]) + len(adj[node2])
                if node2 in adj[node1]:
                    cur -= 1
                ans = max(ans, cur)
        return ans
