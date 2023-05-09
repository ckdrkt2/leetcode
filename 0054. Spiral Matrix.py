from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0: return []

        row1 = col1 = 0
        ans, row2, col2 = [], len(matrix) - 1, len(matrix[0]) - 1

        while row1 <= row2 and col1 <= col2:
            for i in range(col1, col2 + 1):
                ans.append(matrix[row1][i])
            row1 += 1

            for j in range(row1, row2 + 1):
                ans.append(matrix[j][col2])
            col2 -= 1

            if row1 <= row2:
                for x in range(col2, col1 - 1, -1):
                    ans.append(matrix[row2][x])
                row2 -= 1

            if col1 <= col2:
                for k in range(row2, row1 - 1, -1):
                    ans.append(matrix[k][col1])
                col1 += 1

        return ans
