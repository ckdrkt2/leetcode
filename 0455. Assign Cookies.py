from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = idx = 0
        while idx < len(s) and ans < len(g):
            if s[idx] >= g[ans]:
                ans += 1
            idx += 1
        return ans
