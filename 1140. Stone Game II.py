from typing import List
from itertools import accumulate
from functools import cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        acc = [*accumulate(piles[::-1])][::-1]
        @cache
        def dp(i, M):
            if i + 2 * M >= len(acc): return acc[i]
            return acc[i] - min(dp(i + k, max(M, k)) for k in range(1, 2 * M + 1))

        return dp(0, 1)
