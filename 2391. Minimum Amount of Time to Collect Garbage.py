from typing import List
from itertools import accumulate
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel = list(accumulate([0] + travel))
        ans, idx = 0, [0, 0, 0]
        for i, g in enumerate(garbage):
            if "M" in g:
                idx[0] = i
            if "P" in g:
                idx[1] = i
            if "G" in g:
                idx[2] = i
            ans += len(g)
        return ans + sum(travel[i] for i in idx)
