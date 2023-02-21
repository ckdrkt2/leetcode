from typing import List
from functools import reduce
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums, 0)