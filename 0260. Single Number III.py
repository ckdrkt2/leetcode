from typing import List
from functools import reduce
import operator

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = reduce(operator.xor, nums)
        mask, num1 = xor & -xor, 0
        for num in nums:
            if mask & num == 0:
                num1 ^= num

        return [num1, xor^num1]
