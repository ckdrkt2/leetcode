from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        cals = []
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                cals.append(([arr[i], arr[j]], arr[i] / arr[j]))
        return sorted(cals, key=lambda x: x[1])[k - 1][0]
