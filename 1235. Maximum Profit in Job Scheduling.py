from typing import List
from bisect import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        dp = [[0, 0]]
        for s, e, p in sorted(zip(startTime, endTime, profit), key=lambda v: v[1]):
            i = bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]
