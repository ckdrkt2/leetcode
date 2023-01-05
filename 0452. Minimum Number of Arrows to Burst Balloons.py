class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: x[1])
        ans, m = 0, -float('inf')
        for start, end in points:
            if start > m:
                ans += 1
                m = end
        return ans