from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_cnt = max(counter.values())
        max_elements = list(counter.values()).count(max_cnt)
        return max(len(tasks), (max_cnt - 1) * (n + 1) + max_elements)
