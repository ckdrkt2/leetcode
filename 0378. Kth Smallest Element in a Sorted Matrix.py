class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr, N = [m[0] for m in matrix], len(matrix)
        idx = [0] * N
        for _ in range(k):
            ans = min(arr)
            i = arr.index(ans)
            idx[i] += 1
            arr[i] = matrix[i][idx[i]] if idx[i] < N else 1e9
        return ans