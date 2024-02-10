class Solution:


    def countSubstrings(self, s: str) -> int:
        l, ans = len(s), 0
        for i in range(l):
            for j in range(min(i+1, l-i)):
                if s[i-j] == s[i+j]:
                    ans += 1
                else:
                    break
            for j in range(min(i+1, l-i-1)):
                if s[i-j] == s[i+j+1]:
                    ans += 1
                else:
                    break
        return ans
