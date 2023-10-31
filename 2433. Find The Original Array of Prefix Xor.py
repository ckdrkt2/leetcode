from typing import List
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref.pop(0)]
        prev = ans[0]
        for n in pref:
            ans.append(prev ^ n)
            prev = n
        return ans
