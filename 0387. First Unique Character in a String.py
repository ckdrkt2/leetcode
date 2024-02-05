from string import ascii_lowercase


class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = 1e5
        for c in ascii_lowercase:
            l, r = s.find(c), s.rfind(c)
            if l == r != -1:
                ans = min(ans, l)
        return ans if ans < 1e5 else -1
