from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            num, c = i, 0
            while num >= 1:
                c += num % 2
                num = num // 2
            ans.append(c)
        return ans
