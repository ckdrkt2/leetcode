from typing import List
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n, ans = len(arr), 1
        cnt = [0] * (n + 1)

        for num in arr:
            cnt[min(num, n)] += 1

        for num in range(2, n + 1):
            ans = min(ans + cnt[num], num)

        return ans
