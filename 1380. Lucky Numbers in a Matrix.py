from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        a = [0 for i in matrix[0]]
        b = [100000 for i in matrix]
        for m in range(len(matrix)):
            for n in range(len(matrix[0])):
                c = matrix[m][n]
                if c > a[n]:
                    a[n] = c
                if c < b[m]:
                    b[m] = c
        for i in a:
            if i in b: return [i]
