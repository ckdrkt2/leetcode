from typing import List
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        d, ans = Counter(nums), 0
        for n in d:
            if d[n] == 1:
                return -1
            ans += 1 + (d[n] - 1) // 3
        return ans
