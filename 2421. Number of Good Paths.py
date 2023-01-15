from collections import defaultdict, Counter
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        graphs, sameVals = defaultdict(list), defaultdict(set)
        parents = {}
        for u, v in edges:
            sameVals[vals[u]].add(u)
            sameVals[vals[v]].add(v)
            if vals[u] <= vals[v]: graphs[v].append(u)
            if vals[v] <= vals[u]: graphs[u].append(v)

        def find(n):
            parents.setdefault(n, n)
            if parents[n] != n: parents[n] = find(parents[n])
            return parents[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 != p2: parents[p1] = p2

        res = len(vals)

        for val, nodes in sorted(sameVals.items()):
            for node in nodes:
                for neighbor in graphs[node]:
                    union(node, neighbor)
            groups = Counter()
            for node in nodes:
                groups[find(node)] += 1

            for _, cnt in groups.items():
                if cnt >= 2:
                    res += cnt * (cnt - 1) // 2
        return res