from typing import List
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        a = eval('(' + ')*('.join(map(str,nums)) + ')')
        return 1 if a > 0 else -1 if a < 0 else 0