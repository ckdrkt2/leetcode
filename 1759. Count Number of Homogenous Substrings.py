class Solution:
    def countHomogenous(self, s: str) -> int:
        ans = cur = 0

        for i in range(len(s)):
            if i == 0 or s[i] == s[i - 1]:
                cur += 1
            else:
                cur = 1

            ans = (ans + cur) % 1000000007

        return ans
