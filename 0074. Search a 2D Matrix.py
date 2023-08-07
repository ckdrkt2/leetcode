from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) * len(matrix[0]) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            if matrix[row][col] == target: return True
            elif matrix[row][col] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
