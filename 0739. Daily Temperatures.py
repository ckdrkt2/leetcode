from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans, stack = [0] * len(temperatures), []

        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                prev_day = stack.pop()
                ans[prev_day] = i - prev_day
            stack.append(i)

        return ans
