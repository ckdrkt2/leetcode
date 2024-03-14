from typing import List
from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        preSum, ans, mpp = 0, 0, defaultdict(int)
        mpp[0] = 1
        for num in nums:
            preSum += num
            remove = preSum - goal

            if remove in mpp: ans += mpp[remove]

            mpp[preSum] += 1
        return ans
