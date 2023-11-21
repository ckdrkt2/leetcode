from typing import List
from collections import Counter
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        modified = [i - int(str(i)[::-1]) for i in nums]

        return sum(i * (i - 1) // 2 for i in Counter(modified).values()) % 1000000007
