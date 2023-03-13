from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(node1, node2):
            if not (node1 or node2): return True
            if node1 and node2 and node1.val == node2.val:
                return symmetric(node1.left, node2.right) and symmetric(node1.right, node2.left)
            return False
        return symmetric(root.left, root.right)