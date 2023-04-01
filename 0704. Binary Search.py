from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        u, d = len(nums) - 1, 0
        while u >= d:
            v = (u + d) // 2
            if nums[v] == target: return v
            if nums[v] < target: d = v + 1
            else: u = v - 1
        return -1
