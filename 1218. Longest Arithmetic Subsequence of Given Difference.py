from typing import List
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp, ans = {}, 1
        for a in arr:
            b = dp.get(a - difference, 0)
            dp[a] = b + 1
            ans = max(ans, dp[a])
        return ans
