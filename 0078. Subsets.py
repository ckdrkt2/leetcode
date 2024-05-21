from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            ans.extend([ans[i] + [num] for i in range(len(ans))])
        return ans
