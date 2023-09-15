from typing import List
from heapq import heappop, heappush
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, heap = len(points), [(0, 0)]
        in_mst = [False] * n
        ans = used = 0

        while used < n:
            weight, curr_node = heappop(heap)
            if in_mst[curr_node]: continue
            in_mst[curr_node] = True
            ans += weight
            used += 1
            for next_node in range(n):
                if not in_mst[next_node]:
                    next_weight = abs(points[curr_node][0] - points[next_node][0]) + abs(points[curr_node][1] - points[next_node][1])
                    heappush(heap, (next_weight, next_node))

        return ans
