from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = m = 0
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i - 1]:
                m = 0
            ans += min(m, neededTime[i])
            m = max(m, neededTime[i])
        return ans
