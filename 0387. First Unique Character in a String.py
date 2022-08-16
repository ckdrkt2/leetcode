from string import ascii_lowercase

class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = 1e5
        for c in ascii_lowercase:
            l, r = s.find(c), s.rfind(c)
            if l == r != -1: a = min(a, l)
        return a if a < 1e5 else -1