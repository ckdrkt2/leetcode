from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.dfs(root1) == self.dfs(root2)

    def dfs(self, node):
        if not node: return []
        if node.left is None and node.right is None:
            return [node.val]
        return self.dfs(node.left) + self.dfs(node.right)
