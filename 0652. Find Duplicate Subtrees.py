from typing import Optional, List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ans, d = [], defaultdict(int)
        def dfs(node):
            if not node: return "None"
            path = f'{node.val}.{dfs(node.left)}.{dfs(node.right)}'
            d[path] += 1
            if d[path] == 2: ans.append(node)
            return path
        dfs(root)
        return ans
