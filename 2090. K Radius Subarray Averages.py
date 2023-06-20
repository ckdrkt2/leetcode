from typing import List
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0: return nums

        n = len(nums)
        ans = [-1] * n

        if 2 * k + 1 > n: return ans

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        for i in range(k, n - k):
            leftBound, rightBound = i - k, i + k
            subArraySum = prefix[rightBound + 1] - prefix[leftBound]
            average = subArraySum // (2 * k + 1)
            ans[i] = average

        return ans
