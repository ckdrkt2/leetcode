class Solution:
    def profitableSchemes(self, n, minProfit, group, profit):
        dp = [[0] * (n + 1) for i in range(minProfit + 1)]
        dp[0][0] = 1
        for p, g in zip(profit, group):
            for i in range(minProfit, -1, -1):
                for j in range(n - g, -1, -1):
                    dp[min(p + i, minProfit)][g + j] += dp[i][j]
        return sum(dp[minProfit]) % 1000000007
