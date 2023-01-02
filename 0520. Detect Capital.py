class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cnt = 0
        for w in word:
            if w == w.upper(): cnt += 1
        return cnt == len(word) or (cnt == 1 and word[0] == word[0].upper()) or cnt == 0