class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        t = 0
        for i in range(len(columnTitle)-1, -1, -1):
            t += (ord(columnTitle[i]) - 64) * 26**(len(columnTitle)-1-i)
        return t