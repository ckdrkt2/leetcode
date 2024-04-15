from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, '')

    def dfs(self, node: Optional[TreeNode], seen: str) -> int:
        if node.left is None and node.right is None:
            return int(seen + str(node.val))
        result = 0
        if node.left:
            result += self.dfs(node.left, seen + str(node.val))
        if node.right:
            result += self.dfs(node.right, seen + str(node.val))
        return result
        