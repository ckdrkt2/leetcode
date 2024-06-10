from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(e != h for e, h in zip(sorted(heights), heights))
