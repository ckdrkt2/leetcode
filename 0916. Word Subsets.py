from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        c = Counter()
        for word in words2: c |= Counter(word)
        def f(w):
            if c - Counter(w): return False
            return True
        return filter(f, words1)