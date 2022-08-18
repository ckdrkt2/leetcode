from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d, l = Counter(arr), len(arr) - (len(arr) // 2)
        for i, n in enumerate(sorted(d.keys(), key=lambda x : d[x], reverse=True)):
            l -= d[n]
            if l <= 0: break
        return i + 1