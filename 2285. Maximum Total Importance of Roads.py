from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = [0] * n
        for edge in roads:
            degree[edge[0]] += 1
            degree[edge[1]] += 1
        degree.sort()

        ans = 0
        for i, d in enumerate(degree):
            ans += (i + 1) * d

        return ans
