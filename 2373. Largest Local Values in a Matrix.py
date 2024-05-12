from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        length, ans = len(grid), []
        for i in range(length - 2):
            tmp = []
            for j in range(length - 2):
                tmp.append(max(grid[i][j], grid[i][j + 1], grid[i][j + 2],
                           grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2],
                           grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]))
            ans.append(tmp)
        return ans
