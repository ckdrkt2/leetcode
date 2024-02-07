from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(i * Counter(s)[i] for i in sorted(Counter(s), key=lambda x: Counter(s)[x], reverse=True))
