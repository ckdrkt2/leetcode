from typing import List

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []

        for num in nums:
            found = False
            for group in ans:
                if num not in group:
                    found = True
                    group.add(num)
                    break

            if not found:
                ans.append({num})

        return ans
