from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        return min(set(nums1) & set(nums2) if len(set(nums1) & set(nums2)) > 0 else [-1])
