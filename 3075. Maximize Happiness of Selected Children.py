from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        return sum(max(h - i, 0) for i, h in enumerate(sorted(happiness, reverse=True)[:k]))
