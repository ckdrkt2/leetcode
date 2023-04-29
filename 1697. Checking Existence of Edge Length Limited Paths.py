from typing import List
from collections import defaultdict
class Solution:
    def distanceLimitedPathsExist(self, n, edgeList, queries) -> List:
        dict1, n = defaultdict(int), len(queries)
        def find(x):
            if x not in dict1: return x
            else:
                if x != dict1[x]:
                    dict1[x] = find(dict1[x])
                return dict1[x]
        def union(x, y):
            a, b = find(x), find(y)
            if a != b: dict1[b] = a
        edgeList.sort(key=lambda x : x[2])

        i, ans = 0, [False] * n

        for limit, x, y, idx in sorted((q[2], q[0], q[1], i) for i, q in enumerate(queries)):
            while i < len(edgeList) and edgeList[i][2] < limit:
                union(edgeList[i][0], edgeList[i][1])
                i += 1
            ans[idx] = find(x) == find(y)

        return ans
