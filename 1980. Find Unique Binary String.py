from typing import List
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ""
        for i, n in enumerate(nums):
            ans += "1" if n[i] == "0" else "0"
        return ans
