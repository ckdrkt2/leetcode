from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            center = (left + right) // 2
            if sum((p + center - 1) // center for p in piles) > h:
                left = center + 1
            else:
                right = center
        return left