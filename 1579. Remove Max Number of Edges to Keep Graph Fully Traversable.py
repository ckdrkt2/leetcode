class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):

        ufa, ufb = UnionFind(n), UnionFind(n)
        cnt = 0

        for x, y, z in edges:
            if x == 3:
                flag1 = ufa.union(y, z)
                flag2 = ufb.union(y, z)
                if not flag1 or not flag2: cnt += 1

        for x, y, z in edges:
            if x == 1:
                flag = ufa.union(y, z)
                if not flag: cnt += 1
            if x == 2:
                flag = ufb.union(y, z)
                if not flag: cnt += 1

        return cnt if ufa.groups == 1 and ufb.groups == 1 else -1

class UnionFind():
    def __init__(self, n):
        self.parents = {i: i for i in range(1, n + 1)}
        self.groups = n

    def find(self, x):
        if self.parents[x] == x: return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)

        if x == y: return False

        self.parents[y] = x
        self.groups -= 1
        return True