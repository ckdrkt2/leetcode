from string import ascii_lowercase
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i, l = 0, len(s1)
        while i <= len(s2)-l:
            for c in ascii_lowercase:
                d = abs(s1.count(c) - s2[i:i+l].count(c))
                if d > 0: break
            if d == 0: return True
            i += d
        return False