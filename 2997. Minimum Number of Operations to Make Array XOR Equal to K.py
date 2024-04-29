from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = ans = 0

        for n in nums:
            xor ^= n

        while k or xor:
            if (k % 2) != (xor % 2):
                ans += 1
            k //= 2
            xor //= 2
        return ans
