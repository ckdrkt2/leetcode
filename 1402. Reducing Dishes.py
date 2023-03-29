from typing import List
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        total = cur = 0
        for s in satisfaction:
            cur += s
            if cur < 0: break
            total += cur
        return total
