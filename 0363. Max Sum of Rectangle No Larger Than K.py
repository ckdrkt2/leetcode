from bisect import bisect_left, insort
from itertools import combinations, accumulate
class Solution:
    def __init__(self):
        self.ans = -float("inf")
    def maxSumSubmatrix(self, matrix, k):
        def countRangeSum(nums):
            lst = [0]
            for s in accumulate(nums):
                idx = bisect_left(lst, s - k)
                if idx < len(lst): self.ans = max(self.ans, s - lst[idx])
                insort(lst, s)
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                matrix[i][j] += matrix[i - 1][j]
        matrix = [[0] * n] + matrix
        for r1, r2 in combinations(range(m + 1), 2):
            countRangeSum([j - i for i, j in zip(matrix[r1], matrix[r2])])
        return self.ans