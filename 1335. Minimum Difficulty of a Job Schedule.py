class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d: return -1

        # dfs solution -> time limit exceeded
        # def dfs(jobs, days):
        #     if days == 1: return max(jobs)
        #     m = float('inf')
        #     for i in range(1, len(jobs)):
        #         v = max(jobs[:i]) + dfs(jobs[i:], days - 1)
        #         m = min(m, v)
        #     return m
        # return dfs(jobDifficulty, d)

        n = len(jobDifficulty)
        dp = [[300000] * d for _ in range(n)]
        dp[0][0] = jobDifficulty[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], jobDifficulty[i])
        for i in range(1, n):
            for j in range(1, min(i + 1, d)):
                for k in range(i):
                    dp[i][j] = min(dp[i][j], dp[k][j - 1] + max(jobDifficulty[k + 1: i + 1]))
        return dp[-1][-1]