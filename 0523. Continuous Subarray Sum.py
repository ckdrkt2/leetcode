from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash, total = {0: 0}, 0
        for i in range(len(nums)):
            total += nums[i]

            if total % k not in hash:
                hash[total % k] = i + 1

            elif hash[total % k] < i:
                return True

        return False
