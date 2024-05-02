from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        k, nums_set = -1, set(nums)
        for n in nums:
            if n > 0:
                if n > k and -n in nums_set:
                    k = n
        return k
