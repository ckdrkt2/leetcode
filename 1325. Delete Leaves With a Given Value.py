from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root.left:
            self.removeLeafNodes(root.left, target)
        if root.right:
            self.removeLeafNodes(root.right, target)
        if root.left and root.left.val == target and root.left.left == root.left.right == None:
            root.left = None
        if root.right and root.right.val == target and root.right.left == root.right.right == None:
            root.right = None
        return None if root.left == root.right == None and root.val == target else root
