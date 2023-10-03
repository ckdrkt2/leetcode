from typing import List
from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a, b = Counter(nums), 0
        for i in a:
            b += a[i] * (a[i] - 1) // 2
        return b
