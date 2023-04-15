from typing import List
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0] * (k + 1)
        for i in range(len(piles)):
            offset = min(len(piles[i]), k + 1)
            prefix = 0
            last = dp[:]
            for j in range(offset):
                prefix += piles[i][j]
                if i == 0:
                    if j+1 <= k:
                        dp[j+1] = prefix
                else:
                    for p in range(j+1, k+1):
                        dp[p] = max(last[p - (j+1)] + prefix, dp[p])
        return dp[k]
