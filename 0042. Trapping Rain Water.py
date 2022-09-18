class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right, ans = [0] * n, [0] * n, 0

        for i in range(1, n):
            left[i] = max(height[i - 1], left[i - 1])
        for i in range(n - 2, -1, -1):
            right[i] = max(height[i + 1], right[i + 1])

        for h, l, r in zip(height, left, right):
            ans += max(min(l, r) - h, 0)
        return ans