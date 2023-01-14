class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        d = {}

        def find(x):
            d.setdefault(x, x)
            if x != d[x]:
                d[x] = find(d[x])
            return d[x]

        def union(x, y):
            X, Y = find(x), find(y)
            if X > Y:
                d[X] = Y
            else:
                d[Y] = X

        for i in range(len(s1)):
            union(s1[i], s2[i])

        res = []
        for c in baseStr:
            res.append(find(c))

        return ''.join(res)