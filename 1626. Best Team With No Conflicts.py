class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        dp = [0] * (1 + max(ages))
        for score, age in sorted(zip(scores, ages)):
            dp[age] = score + max(dp[:age + 1])
        return max(dp)