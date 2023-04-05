from typing import List
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = total = 0
        for i, n in enumerate(nums):
            total += n
            ans = max(ans, (total + i) // (i + 1))
        return ans
