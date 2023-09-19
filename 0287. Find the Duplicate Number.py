from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = set()
        for n in nums:
            if n in ans: return n
            ans.add(n)
