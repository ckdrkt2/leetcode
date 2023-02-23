from typing import List
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = []
        for p, c in zip(profits, capital): projects.append((p, c))
        projects.sort(key=lambda x: x[0], reverse=True)
        for _ in range(k):
            prev = w
            for i, (p, c) in enumerate(d):
                if c <= w:
                    w += p
                    projects.pop(i)
                    break
            if prev == w: break
        return w