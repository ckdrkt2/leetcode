from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, miss = Counter(t), len(t)
        i = a = b = 0
        for j, c in enumerate(s, 1):
            miss -= need[c] > 0
            need[c] -= 1
            if not miss:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not b or j - i <= b - a:
                    a, b = i, j
        return s[a:b]
