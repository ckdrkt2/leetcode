from typing import List

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        freq = [0] * (n + max(nums) + 1)

        for num in nums:
            freq[num] += 1

        for i in range(len(freq)):
            if freq[i] <= 1: continue

            dup, freq[i] = freq[i] - 1, 1
            freq[i + 1] += dup
            ans += dup

        return ans
