from itertools import permutations
class Solution:
    def largestVariance(self, s: str) -> int:
        ans = 0
        for _ in range(2):
            for a, b in permutations(set(s), 2):
                c1 = c2 = 0
                for c in s:
                    if c == a: c1 += 1
                    elif c == b: c2 += 1
                    else: continue

                    if c2 > c1: c1 = c2 = 0
                    elif c1 > 0 and c2 > 0:
                        ans = max(ans, c1 - c2)
            s = s[::-1]

        return ans
