from typing import List
from heapq import heappush, heappop
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans, heap = [], []
        heappush(heap, (nums1[0] + nums2[0], 0, 0))
        while heap and len(ans) < k:
            pair_sum, i, j = heappop(heap)
            ans.append((nums1[i], nums2[j]))
            if i < len(nums1) and j + 1 < len(nums2):
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            if i + 1 < len(nums1) and j == 0:
                heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
        return ans
