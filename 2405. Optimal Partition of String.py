class Solution:
    def partitionString(self, s: str) -> int:
        ans, p = 0, set()
        for c in s:
            if c in p:
                ans += 1
                p = set()
            p.add(c)
        return ans + 1