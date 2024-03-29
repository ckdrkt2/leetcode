from functools import cache
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        @cache
        def dp(i, max_so_far, remain):
            if i == n:
                if remain == 0: return 1
                return 0
            ans = (max_so_far * dp(i + 1, max_so_far, remain)) % 1000000007
            for num in range(max_so_far + 1, m + 1):
                ans = (ans + dp(i + 1, num, remain - 1)) % 1000000007
            return ans
        return dp(0, 0, k)