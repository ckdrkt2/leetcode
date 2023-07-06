from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = total = 0
        ans = float('inf')
        for right, n in enumerate(nums):
            total += n
            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1
        return ans if ans <= len(nums) else 0
