from typing import List
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        pc = Counter(p)
        sc = Counter(s[:len(p)-1])
        for i in range(len(p)-1, len(s)):
            sc[s[i]] += 1
            if sc == pc: ans.append(i - len(p) + 1)
            sc[s[i - len(p) + 1]] -= 1
        return ans