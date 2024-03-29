from typing import List
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        a, b = {}, []
        for i, n in enumerate(groupSizes):
            if n not in a: a[n] = [i]
            else: a[n].append(i)
        for i in sorted(a):
            for j in range(0, len(a[i]), i):
                b.append(a[i][j:j+i])
        return b
