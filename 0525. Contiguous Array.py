from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        index = {0: -1}
        ans = cnt = 0
        for i, num in enumerate(nums):
            cnt += 1 if num == 1 else -1
            if cnt in index:
                ans = max(ans, i - index[cnt])
            else:
                index[cnt] = i
        return ans
