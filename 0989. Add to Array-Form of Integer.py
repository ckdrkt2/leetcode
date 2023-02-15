from typing import List
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return map(int, list(str(eval(''.join(map(str, num)) + '+' + str(k)))))