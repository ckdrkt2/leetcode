from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return [word for word in words + [""] if word == word[::-1]][0]
