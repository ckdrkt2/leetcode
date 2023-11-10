from typing import List
from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph, ans = defaultdict(list), []
        for i, j in adjacentPairs:
            graph[i].append(j)
            graph[j].append(i)

        for i, j in graph.items():
            if len(j) == 1:
                ans += [i, j[0]]
                break

        for i in range(len(adjacentPairs) - 1):
            x, y = graph[ans[-1]]
            if x == ans[-2]:
                ans.append(y)
            else:
                ans.append(x)
        return ans
