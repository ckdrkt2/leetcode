from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, root.val, root.val)

    def dfs(self, node, left, right) -> int:
        if node is None:
            return 0

        left, right = min(left, node.val), max(right, node.val)
        return max(abs(node.val - left), abs(node.val - right), self.dfs(node.left, left, right), self.dfs(node.right, left, right))
