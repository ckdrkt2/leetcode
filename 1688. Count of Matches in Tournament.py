class Solution:
    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            if n % 2:
                ans += n // 2
                n = n // 2 + 1
            else:
                n = n // 2
                ans += n
        return ans
