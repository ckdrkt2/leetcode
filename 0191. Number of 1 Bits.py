class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum((n >> i) & 1 for i in range(32))
