class Solution:
    def pivotInteger(self, n: int) -> int:
        return int(((n * n + n) // 2) ** 0.5) if int(((n * n + n) // 2) ** 0.5) ** 2 == (n * n + n) // 2 else -1
