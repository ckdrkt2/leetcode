from typing import List
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = [0] * n
        for start, end in edges: ans[end] += 1
        return [i for i in range(n) if ans[i] == 0]