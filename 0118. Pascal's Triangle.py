from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ex, now, ans = [1], [], []
        for i in range(numRows):
            for j in range(i+1):
                if j == i or j == 0:
                    now.append(1)
                else:
                    now.append(ex[j-1] + ex[j])
            ans.append(now)
            ex, now = [n for n in now], []
        return ans
