from typing import List

# Approach 1: Using Bit Manipulation
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans, bits = [], 0
        for num in nums:
            if (bits >> num) & 1 == 0:
                bits ^= 1 << num
            else:
                ans.append(num)
        return ans

# Approach 2: Using Hash Table
class Solution2:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            idx = abs(num)
            if nums[idx - 1] < 0:
                ans.append(idx)
            nums[idx - 1] *= -1
        return ans
