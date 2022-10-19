from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return sorted(Counter(words), key=lambda x : (-d[x], x))[:k]