from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = c = 0
        for n in nums:
            if c == 0:
                ans = n
            c += (1 if n == ans else -1)
        return ans
