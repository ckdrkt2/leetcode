from collections import defaultdict
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for _ in range(len(nums))]
        ans = 0
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[j] - nums[i]
                ans += dp[j][diff]
                dp[i][diff] += dp[j][diff] + 1
        return ans