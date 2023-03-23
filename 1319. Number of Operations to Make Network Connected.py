from typing import List
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1

        def find(roots, i):
            while roots[i] is not i:
                roots[i] = roots[roots[i]]
                i = roots[i]
            return i
        roots, ans = [i for i in range(n)], n
        for x, y in connections:
            root1 = find(roots, x)
            root2 = find(roots, y)
            if root1 is not root2:
                roots[root1] = root2
                ans -= 1
        return ans - 1