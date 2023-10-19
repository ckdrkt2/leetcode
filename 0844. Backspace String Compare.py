class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s):
            if s[i] == '#':
                if i > 0:
                    s = s[:i-1] + s[i+1:]
                    i -= 1
                else:
                    s = s[1:]
            else:
                i += 1
        while j < len(t):
            if t[j] == '#':
                if j > 0:
                    t = t[:j-1] + t[j+1:]
                    j -= 1
                else:
                    t = t[1:]
            else:
                j += 1
        return s == t
