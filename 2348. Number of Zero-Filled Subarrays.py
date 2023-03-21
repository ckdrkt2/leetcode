from typing import List
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = cnt = 0
        nums.append(1)
        for n in nums:
            if n: cnt = 0
            else: cnt += 1
            ans += cnt
        return ans
