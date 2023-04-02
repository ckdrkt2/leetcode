from typing import List
from bisect import bisect_left
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        for s in spells:
            idx = bisect_left(potions, (success//s) + bool(success % s))
            ans.append(len(potions) - idx)
        return ans
