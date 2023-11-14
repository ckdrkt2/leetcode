class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = {}
        for i in range(len(s) - 2):
            head = s[i]
            if head in ans: continue
            for j in range(len(s) - 1, i + 1, -1):
                if head == s[j]:
                    ans[head] = len(set(s[i + 1: j]))
                    break
        return sum(ans.values())
