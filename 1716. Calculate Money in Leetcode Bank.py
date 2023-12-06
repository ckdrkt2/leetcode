class Solution:
    def totalMoney(self, n: int) -> int:
        ans, cnt = 0, 1

        while n > 0:
            for day in range(min(n, 7)):
                ans += cnt + day

            n -= 7
            cnt += 1

        return ans
