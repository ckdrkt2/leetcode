from typing import List

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        if m == 2: return position[-1] - position[0]

        left, right = 0, (position[-1] - position[0]) // (m - 1) + 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if self.check(position, mid, m):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def check(self, position, distance, m):
        cnt, prev = 1, position[0]
        for p in position[1:]:
            if p - prev >= distance:
                cnt += 1
                prev = p
        return cnt >= m
