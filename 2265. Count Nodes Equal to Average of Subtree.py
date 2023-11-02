from typing import Optional, List
from math import floor

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> (int, List):
            if not node: return 0, []

            cnt1, left = dfs(node.left)
            cnt2, right = dfs(node.right)

            nums = left + [node.val] + right
            cnt = cnt1 + cnt2 + int(floor(sum(nums) / len(nums)) == node.val)

            return cnt, nums

        ans, _ = dfs(root)

        return ans
