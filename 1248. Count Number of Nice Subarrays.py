from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = gap = length = start = 0

        for end in range(len(nums)):
            if nums[end] % 2 == 1:
                length += 1
            if length == k:
                gap = 0
                while length == k:
                    length -= nums[start] % 2
                    gap += 1
                    start += 1
            ans += gap

        return ans
