from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2: return len(points)

        def f(p1, p2):
            if p1[0] - p2[0] == 0: return float('inf')
            return (p1[1] - p2[1]) / (p1[0] - p2[0])

        ans = 1
        for i in range(0, len(points)):

            slopes = defaultdict(int)
            for j in range(i + 1, len(points)):
                slope = f(points[i], points[j])
                slopes[slope] += 1
                ans = max(slopes[slope], ans)
        return ans + 1
