from typing import List
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n, ans = len(weights), 0
        pairs = [0] * (n - 1)
        for i in range(n - 1):
            pairs[i] = weights[i] + weights[i + 1]
        pairs.sort()

        return sum(pairs[n - 2 - i] - pairs[i] for i in range(k - 1))
