class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans = k = 0
        mask = 1

        while mask <= n:
            if n & mask:
                ans = 2 ** (k + 1) - 1 - ans

            mask <<= 1
            k += 1

        return ans
