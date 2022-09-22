class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s[::-1].split()))