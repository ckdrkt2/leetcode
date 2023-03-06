from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num, i = 1, 0
        for _ in range(k):
            while i < len(arr) and num == arr[i]:
                num += 1
                i += 1
            num += 1
        return num - 1