class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = cnt = 0
        vowels = "aeiou"
        for i, v in enumerate(s):
            if i >= k and s[i-k] in vowels: cnt -= 1
            if s[i] in vowels: cnt += 1
            ans = max(cnt, ans)
        return ans
