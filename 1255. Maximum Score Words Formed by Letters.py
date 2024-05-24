from collections import Counter
from itertools import combinations
from string import ascii_lowercase

class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        alphabet = {a:i for i, a in enumerate(ascii_lowercase)}
        scores, ans = {}, 0
        for word in words:
            scores[word] = sum([score[alphabet[w]] for w in word])
        words = sorted(words, key = lambda x : scores[x], reverse=True)

        all_subset = []
        for i in range(1, len(words)+1):
            all_subset += list(combinations(words, i))
        for subset in all_subset:
            dd = self.check(subset, Counter(letters), scores)
            ans = max(ans, dd)
        return ans

    def check(self, words: list[str], count: dict, scores: dict) -> int:
        total = 0
        for word in words:
            word_count = Counter(word)
            if len(word_count) > sum([word_count[w] <= count[w] for w in word_count]): continue
            total += scores[word]
            for w in word_count:
                count[w] -= word_count[w]
        return total
