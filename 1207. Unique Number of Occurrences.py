from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(arr)) == len(set(Counter(arr).values()))
