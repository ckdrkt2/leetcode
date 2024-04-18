from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        
        for row_ind, row in enumerate(grid):
            for col_ind, land in enumerate(row):
                if not land:
                    continue
                ans += 4
                    
                if col_ind and row[col_ind-1]:
                    ans -= 2
                    
                if row_ind and grid[row_ind-1][col_ind]:
                    ans -= 2
                    
        return ans
        