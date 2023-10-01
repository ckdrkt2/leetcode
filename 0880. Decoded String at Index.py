class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        ans = ""
        for c in s:
            if c.isalpha():
                ans += c
            else:
                ans *= c
        return ans
