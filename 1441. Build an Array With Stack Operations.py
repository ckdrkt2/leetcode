from typing import List
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans, j = [], 1
        for i in target:
            ans = ans + ["Push", "Pop"] * (i - j) + ["Push"]
            j = i + 1
        return ans
