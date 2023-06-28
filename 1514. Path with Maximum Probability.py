from typing import List
from collections import defaultdict
from heapq import heappop, heappush
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        max_prob = [0.0] * n
        max_prob[start] = 1.0

        heap = [(-1.0, start)]
        while heap:
            cur_prob, cur_node = heappop(heap)
            if cur_node == end: return -cur_prob
            for nxt_node, path_prob in graph[cur_node]:
                if -cur_prob * path_prob > max_prob[nxt_node]:
                    max_prob[nxt_node] = -cur_prob * path_prob
                    heappush(heap, (-max_prob[nxt_node], nxt_node))
        return 0.0
