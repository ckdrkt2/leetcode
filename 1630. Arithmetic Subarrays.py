from typing import List
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def f(b):
            gap = b[-1] - b[-2]
            for j in range(len(b)-1):
                if b[j+1] - b[j] != gap:
                    return False
            return True

        ans = []
        for i in range(len(l)):
            ans.append(f(sorted([nums[i] for i in range(l[i], r[i]+1)])))
        return ans
