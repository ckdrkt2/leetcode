from typing import List
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 0, min(time) * totalTrips
        while left < right:
            center = (left + right) // 2
            trips = sum(map(lambda x: center // x, time))
            if trips >= totalTrips:
                right = center
            else:
                left = center + 1
        return left