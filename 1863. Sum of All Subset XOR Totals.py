from typing import List
from functools import reduce
from operator import or_

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return reduce(or_, nums) << len(nums) - 1
