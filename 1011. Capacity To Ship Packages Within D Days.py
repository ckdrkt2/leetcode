from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (right + left) // 2
            day, cap = 1, 0
            for weight in weights:
                if cap + weight > mid:
                    day += 1
                    cap = weight
                else:
                    cap += weight
            if day <= days: right = mid
            else: left = mid + 1
        return left