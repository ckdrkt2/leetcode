from typing import List
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        ans = sum(batteries)
        while batteries[-1] > ans // n:
            n -= 1
            ans -= batteries.pop()
        return ans // n
