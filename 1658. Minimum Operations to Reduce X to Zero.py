from typing import List
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        numsSum = sum(nums)
        if numsSum < x: return -1
        if numsSum == x: return len(nums)
        
        requiredSum = numsSum - x
        maxLength = left = currSum = 0
        
        for right, num in enumerate(nums):
            currSum += num
            while currSum > requiredSum:
                currSum -= nums[left]
                left +=1
            if currSum == requiredSum:
                maxLength = max(maxLength, right - left + 1)
        return len(nums) - maxLength if maxLength > 0 else -1
