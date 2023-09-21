from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n: nums1, nums2, m, n = nums2, nums1, n, m

        lo, hi = 0, m
        while lo <= hi:
            x = (lo + hi) // 2
            y = (m + n + 1) // 2 - x
            maxX = -1000000 if x == 0 else nums1[x - 1]
            maxY = -1000000 if y == 0 else nums2[y - 1]
            minX = 1000000 if x == m else nums1[x]
            minY = 1000000 if y == n else nums2[y]

            if maxX <= minY and maxY <= minX:
                if (m + n) % 2:
                    return max(maxX, maxY)
                else:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
            elif maxX > minY:
                hi = x - 1
            else:
                lo = x + 1
