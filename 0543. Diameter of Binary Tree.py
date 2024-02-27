from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.diameter

    def dfs(self, node):
        if node is None: return 0

        left, right = self.dfs(node.left), self.dfs(node.right)
        self.diameter = max(self.diameter, left + right)
        return max(left, right) + 1
