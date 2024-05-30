from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0

        for i in range(len(arr)):
            num = arr[i]
            for j in range(i + 1, len(arr)):
                num ^= arr[j]
                if num == 0:
                    ans += j - i

        return ans
