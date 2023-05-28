from typing import List
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        c, cuts = len(cuts), [0] + sorted(cuts) + [n]
        dp = [[0 for _ in range(c + 2)] for _ in range(c + 2)]
        for i in range(c, 0, -1):
            for j in range(1, c + 1):
                if i > j: continue
                ans = 1e8
                for idx in range(i, j + 1):
                    val = cuts[j + 1] - cuts[i - 1] + dp[i][idx - 1] + dp[idx + 1][j]
                    ans = min(ans, val)
                dp[i][j] = ans
        return dp[1][c]
