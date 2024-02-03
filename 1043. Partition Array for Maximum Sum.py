from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        ans = [0] * (len(arr)+1)
        for i in range(1, len(arr)+1):
            m = 0
            for j in range(1, min(k, i) + 1):
                m = max(m, arr[i - j])
                ans[i] = max(ans[i], ans[i - j] + m * j)

        return ans[-1]
