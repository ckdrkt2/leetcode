from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0: return 1
        dp = [[0]*(amount+1) for _ in range(len(coins))]
        for i in range(len(coins)):
            for j in range(1, amount+1):
                if i >= 0:
                    dp[i][j] += dp[i-1][j]
                if j == coins[i]:
                    dp[i][j] += 1
                elif j > coins[i]:
                    dp[i][j] += dp[i][j-coins[i]]

        return dp[-1][-1]
