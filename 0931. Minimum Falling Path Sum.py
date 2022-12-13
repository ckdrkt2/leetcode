class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = matrix.pop(0)
        for i, line in enumerate(matrix):
            b = [float('inf')] + m + [float('inf')]
            for j, arr in enumerate(zip(b[:-2],b[1:-1],b[2:])):
                m[j] = min(arr) + line[j]
        return min(m)