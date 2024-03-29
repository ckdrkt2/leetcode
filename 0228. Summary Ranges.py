from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        ans, s, ex = [], "", None
        for i, n in enumerate(nums):
            if not s:
                s += str(n)
            elif n - ex > 1:
                if int(s) == ex:
                    ans.append(s)
                else:
                    ans.append(s + '->' + str(ex))
                s = str(n)
            ex = n
        if int(s) == ex:
            ans.append(s)
        else:
            ans.append(s + '->' + str(ex))
        return ans
