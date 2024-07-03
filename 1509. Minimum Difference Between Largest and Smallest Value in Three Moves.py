from typing import List

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5: return 0
        nums.sort()
        ans = 2000000000
        for i in range(4):
            ans = min(ans, nums[-4 + i] - nums[i])
        return ans
