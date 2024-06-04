from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = Counter(s)
        b = c = 0
        for i in a:
            if not a[i] % 2:
                b += a[i]
            else:
                b += a[i] - 1
                c = 1
        return b + c
