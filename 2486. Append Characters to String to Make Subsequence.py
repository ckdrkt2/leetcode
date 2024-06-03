class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n, iters = len(t), iter(s)
        for i, c in enumerate(t):
            if c not in iters:
                return n - i
        return 0
