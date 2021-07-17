class Solution:
    def hammingWeight(self, n: int) -> int:
        return len(bin(n)[2:].replace("0", ""))
        