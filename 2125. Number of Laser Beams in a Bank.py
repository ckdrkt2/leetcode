from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ex, ans = bank.pop(0).count('1'), 0
        for i, b in enumerate(bank):
            cur = b.count('1')
            if not cur: continue
            ans += ex * cur
            ex = cur
        return ans
