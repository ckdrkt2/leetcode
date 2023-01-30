class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0, 1, 1]
        for _ in range(n-2): arr.append(sum(arr[-3:]))
        return arr[n]