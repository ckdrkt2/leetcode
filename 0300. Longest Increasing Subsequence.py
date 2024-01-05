from typing import List
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [nums.pop(0)]
        for n in nums:
            if n > ans[-1]: 
                ans.append(n)
            else: 
                ans[bisect_left(ans, n)] = n
        return len(ans)
