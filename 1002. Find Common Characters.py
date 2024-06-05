from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return words
        ans, sets = [], set(words[0])
        for i in sets:
            n = min([j.count(i) for j in words])
            ans += [i] * n
        return ans
