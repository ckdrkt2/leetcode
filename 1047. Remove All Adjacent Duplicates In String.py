class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = ""
        for c in s:
            if ans and ans[-1] == c:
                ans = ans[:-1]
            else:
                ans += c
        return ans