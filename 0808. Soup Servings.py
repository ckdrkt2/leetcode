from collections import defaultdict
class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 4800: return 1
        stack = {(n, n): 1}
        dirs = {(100, 0), (75, 25), (50, 50), (25, 75)}
        ans = 0
        while stack:
            new = defaultdict(float)
            for a, b in stack:
                t = stack[a, b] * 0.25
                if t < 0.00000001: continue
                for x, y in dirs:
                    a0, b0 = a - x, b - y
                    if a0 > 0 and b0 > 0:
                        new[a0, b0] += t
                    elif a0 <= 0 < b0:
                        ans += t
                    elif a0 <= 0 and b0 <= 0:
                        ans += t / 2
            stack = dict(new)
        return ans
