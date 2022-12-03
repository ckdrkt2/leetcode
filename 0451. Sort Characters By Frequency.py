from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        return ''.join(i * c[i] for i in sorted(c, key=lambda x : c[x], reverse=True))