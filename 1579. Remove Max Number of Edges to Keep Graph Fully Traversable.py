from typing import List

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice, bob = UnionFind(n), UnionFind(n)

        cnt = sum((alice.union(src, dst) | bob.union(src, dst)) for type, src, dst in edges if type == 3)
        for type, src, dst in edges:
            cnt += (alice if type == 1 else bob).union(src, dst)

        return (len(edges) - cnt) if bob.isConnected() and alice.isConnected() else -1

class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = list(range(n + 1))
        self.rank = [1] * (n + 1)

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        self.n -= 1
        return True

    def isConnected(self):
        return self.n == 1
