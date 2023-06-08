from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for row in grid:
            lo, hi = 0, len(grid[0]) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if row[mid] < 0:
                    hi = mid - 1
                else:
                    lo = mid + 1
            ans += (len(grid[0]) - lo)
        return ans
