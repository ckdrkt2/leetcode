from typing import List
class Solution:
   def longestSubarray(self, nums: List[int]) -> int:
        m, n = 0, 1
        for i in range(len(nums)):
            n -= nums[i] == 0
            if n < 0:
                n += nums[m] == 0
                m += 1
        return i - m
