from collections import Counter

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a, b, ans = Counter(s), Counter(t), 0
        for i in a:
            if i in b:
                ans += a[i] - b[i] if a[i] > b[i] else 0
            else:
                ans += a[i]
        return ans
