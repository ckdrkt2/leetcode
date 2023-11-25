from typing import List
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        a, b, ans, l = sum(nums), 0, [], len(nums)
        for i, n in enumerate(nums):
            ans.append(a - n * l + 2 * n * i - b)
            a -= n
            b += n
        return ans
