from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums)**2 + len(nums)) // 2 - sum(nums)
