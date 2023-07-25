from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        a, b = 1, len(arr) - 2
        while a <= b:
            i = (a + b) // 2
            if arr[i] > arr[i+1]:
                b = i - 1
            else:
                a = i + 1
        return a
