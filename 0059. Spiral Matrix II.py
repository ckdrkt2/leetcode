from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        direct, num = ((0, 1), (1, 0), (0, -1), (-1, 0)), 1
        k = i = j = 0
        while num <= n ** 2:
            ans[i][j] = num
            num += 1
            x, y = direct[k]
            if not (0 <= i + x < n) or not (0 <= j + y < n) or ans[i + x][j + y] != 0:
                k = (k + 1) % 4
                x, y = direct[k]
            i += x
            j += y
        return ans
