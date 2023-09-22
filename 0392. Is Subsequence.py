class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            a = t.find(i)
            if a != -1:
                t = t[a+1:]
            else:
                return False
        return True
