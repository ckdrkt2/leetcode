class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        n = len(s1)
        for k in range(1, n):
            if self.isScramble(s1[0:k], s2[0:k]) and self.isScramble(s1[k:], s2[k:]):
                return True
            if self.isScramble(s1[0:k], s2[n - k:]) and self.isScramble(s1[k:], s2[:n - k]):
                return True
        return False