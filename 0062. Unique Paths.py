from math import factorial as f
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return f(m + n - 2) // (f(m - 1) * f(n - 1))
