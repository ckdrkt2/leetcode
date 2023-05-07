from typing import List
from bisect import bisect_right
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        ans, lst = [1] * len(obstacles), []

        for i, height in enumerate(obstacles):
            idx = bisect_right(lst, height)

            if idx == len(lst):
                lst.append(height)
            else:
                lst[idx] = height
            ans[i] = idx + 1

        return ans
