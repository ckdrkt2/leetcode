class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        d = {_ : 0 for _ in arr}
        for i, n in enumerate(arr):
            c = 1
            for x in arr[:i]:
                if n % x: continue
                y = n // x
                c += d.get(x,0) * d.get(y,0)
            d[n] = c
        return sum(d.values()) % 1000000007