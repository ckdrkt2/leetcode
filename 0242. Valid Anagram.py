class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for n in range(97, 97+26):
            if s.count(chr(n)) != t.count(chr(n)):
                return False
        return True