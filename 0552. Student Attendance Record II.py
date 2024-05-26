class Solution:
    def checkRecord(self, n: int) -> int:
        if n < 5:
            return [3, 8, 19, 43][n - 1]

        MOD = 1000000007
        a0, a1, a2, a3 = 2, 4, 7, 13
        r0, r1, r2, r3 = 3, 8, 19, 43

        for i in range(4, n):
            x = a3 - a0
            r0, r1, r2, r3 = r1, r2, r3, ((r3 << 1) - r0 + x) % MOD
            a0, a1, a2, a3 = a1, a2, a3, (a3 + x) % MOD

        return r3
