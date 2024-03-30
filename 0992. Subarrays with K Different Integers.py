from typing import List
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.f(nums, k) - self.f(nums, k - 1)

    def f(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        ans = left = 0
        for right, num in enumerate(nums):
            counter[num] += 1
            while len(counter) > k:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                left += 1
            ans += right - left + 1
        return ans
