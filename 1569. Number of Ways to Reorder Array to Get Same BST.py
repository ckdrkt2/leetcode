from typing import List
from math import comb

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def dfs(nums):
            if len(nums) < 3: return 1
            left_nodes = [a for a in nums if a < nums[0]]
            right_nodes = [a for a in nums if a > nums[0]]
            return dfs(left_nodes) * dfs(right_nodes) * comb(len(nums) - 1, len(left_nodes))

        return (dfs(nums) - 1) % 100000007
