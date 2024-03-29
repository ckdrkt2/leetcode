from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        idx = [i for i, num in enumerate(nums) if num == max_num]

        ans, ex, length = 0, -1, len(nums)
        for i in range(len(idx) - k + 1):
            left, right = idx[i], idx[i + k - 1]
            ans += (left - ex) * (length - right)
            ex = left

        return ans
