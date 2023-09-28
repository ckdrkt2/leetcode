from typing import List
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                nums.append(nums[i])
                nums[i] = -1
        for _ in range(nums.count(-1)):
            nums.remove(-1)
        return nums
