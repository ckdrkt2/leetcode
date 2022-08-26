from collections import Counter
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return any(Counter(str(n)) == Counter(str(1 << i)) for i in range(31))