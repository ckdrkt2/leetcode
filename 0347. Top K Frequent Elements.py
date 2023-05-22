from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        return sorted(a.keys(), key=lambda x: a[x], reverse=True)[:k]
