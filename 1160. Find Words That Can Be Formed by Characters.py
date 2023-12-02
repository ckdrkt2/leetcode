from collections import Counter
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        length, count = [], Counter(chars)
        for word in words:
            for char in word:
                if count[char] < word.count(char):
                    break
            else:
                length.append(len(word))
        return sum(length)
