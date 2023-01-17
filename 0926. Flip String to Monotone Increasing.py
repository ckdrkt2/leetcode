class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        cnt0, cnt1 = s.count('0'), 0
        ans = n - cnt0
        for i in range(n):
            if s[i] == '0':
                cnt0 -= 1
            elif s[i] == '1':
                ans = min(ans, cnt0 + cnt1)
                cnt1 += 1
        return ans