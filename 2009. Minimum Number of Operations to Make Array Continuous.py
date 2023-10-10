from typing import List
from bisect import bisect_right
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = n = len(nums)
        new_nums = sorted(set(nums))

        for i in range(len(new_nums)):
            left = new_nums[i]
            right = left + n - 1
            count = bisect_right(new_nums, right) - i
            ans = min(ans, n - count)
        return ans
