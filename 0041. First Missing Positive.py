from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            if nums[i] < 1:
                nums[i] = N + 1
        for num in nums:
            val = abs(num)
            if val > len(nums): continue
            if nums[val - 1] > 0:
                nums[val - 1] *= -1
        for i in range(N):
            if nums[i] > 0:
                return i + 1

        return N + 1
