from typing import List
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = [0] * n, [n - 1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                idx = stack.pop()
                right[idx] = i - 1
            left[i] = stack[-1] + 1 if stack else 0
            stack.append(i)

        ans = 0
        for i in range(n):
            if right[i] < k or left[i] > k: continue
            ans = max(ans, nums[i] * (right[i] - left[i] + 1))

        return ans
