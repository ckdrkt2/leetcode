class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if word.find(ch)>= 0:
            x = word.find(ch)
            w = word[:x+1]
            return w[::-1] + word[x+1:]
        return word
