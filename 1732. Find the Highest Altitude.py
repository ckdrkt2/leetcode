from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans, tot = 0, 0
        for n in gain:
            tot += n
            ans = max(ans, tot)
        return ans
