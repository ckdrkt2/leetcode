from typing import List
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]: continue
            elements = (nums[i] + nums[i + 1] - 1) // nums[i + 1]
            ans += elements - 1
            nums[i] = nums[i] // elements
        return ans
