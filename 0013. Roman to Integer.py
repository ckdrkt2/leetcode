class Solution:
    def romanToInt(self, s: str) -> int:
        a = list(s[::-1]); n = 0; t = 0
        for i in range(len(a)):
            if a[i] == 'I':
                a[i] = 1
            elif a[i] == 'V':
                a[i] = 5
            elif a[i] == 'X':
                a[i] = 10
            elif a[i] == 'L':
                a[i] = 50
            elif a[i] == 'C':
                a[i] = 100
            elif a[i] == 'D':
                a[i] = 500
            elif a[i] == 'M':
                a[i] = 1000
            if a[i] >= n:
                n = a[i]
                t += a[i]
            else:
                t -= a[i]
        return t