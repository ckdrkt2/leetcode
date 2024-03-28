from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        ans = length = i = 0
        for num in nums:
            cnt[num] += 1
            length += 1
            if cnt[num] <= k:
                ans = max(ans, length)
            else:
                while cnt[num] > k:
                    cnt[nums[i]] -= 1
                    length -= 1
                    i += 1
        return ans
