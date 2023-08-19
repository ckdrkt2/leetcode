# NOT MY SOLUTION!

from typing import List
from collections import defaultdict
class Union:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            if self.rank[pa] >= self.rank[pb]:
                self.parent[pb] = pa
                if self.rank[pa] == self.rank[pb]:
                    self.rank[pa] += 1
            else:
                self.parent[pa] = pb
    def find(self, a):
        pa = self.parent[a]
        if pa != self.parent[pa]:
            self.parent[a] = self.find(pa)
        return self.parent[a]

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        dsu = Union(n)
        curAdjs, levels, lows, curLevel = dict(), list(), list(), [0]
        ans = [[], []]
        mark = [-1] * len(edges)

        def tarjan(cur, prev):
            levels[cur], lows[cur], curLevel[0] = curLevel[0], curLevel[0], curLevel[0] + 1
            for (ind, c) in curAdjs[cur]:
                dsu.union(cur, c)
                if levels[c] == -1:
                    tarjan(c, ind)
                    lows[cur] = min(lows[cur], lows[c])
                    if lows[c] > levels[cur]:
                        mark[ind] = 0
                    else:
                        mark[ind] = 1
                elif ind != prev:
                    lows[cur] = min(lows[cur], levels[c])
                    mark[ind] = 1

        myEdges = defaultdict(list)
        for i in range(len(edges)):
            myEdges[edges[i][2]].append((i, edges[i][0], edges[i][1]))
        weights = sorted(myEdges.keys())
        for w in weights:
            curAdjs = defaultdict(list)
            levels, lows, curLevel[0] = [-1] * n, [-1] * n, 0
            for (ind, a, b) in myEdges[w]:
                pa, pb = dsu.find(a), dsu.find(b)
                if pa != pb:
                    curAdjs[pa].append((ind, pb))
                    curAdjs[pb].append((ind, pa))
            for cur in curAdjs.keys():
                if levels[cur] == -1:
                    tarjan(cur, -1)
        for i in range(len(edges)):
            if mark[i] != -1:
                ans[mark[i]].append(i)
        return ans
