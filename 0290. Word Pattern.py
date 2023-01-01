class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p, c = pattern, s.split()
        return list(map(p.find, p)) == list(map(c.index, c))