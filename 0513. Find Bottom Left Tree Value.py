from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)[0]

    def dfs(self, node: Optional[TreeNode], depth: int) -> Tuple[int, int]:
        if node is None: return -1, -1

        left, right = self.dfs(node.left, depth + 1), self.dfs(node.right, depth + 1)
        if left[1] == right[1] == -1:
            return node.val, depth
        elif left[1] >= right[1]:
            return left
        else:
            return right
