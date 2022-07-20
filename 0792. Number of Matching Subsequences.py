from collections import defaultdict
from bisect import bisect_left

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def check(word):
            cur = 0
            for w in word:
                idx = bisect_left(places[w], cur)
                if idx >= len(places[w]): return 0
                cur = places[w][idx] + 1
            return 1

        places = defaultdict(list)
        for i, c in enumerate(s):
            places[c].append(i)

        return sum(check(word) for word in words)