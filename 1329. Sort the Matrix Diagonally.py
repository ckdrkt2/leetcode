from collections import defaultdict
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                d[r-c].append(mat[r][c])
        for v in d.values():
            v.sort(reverse=True)
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                mat[r][c] = d[r-c].pop()
        return mat