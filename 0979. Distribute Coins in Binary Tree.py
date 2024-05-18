from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def DFS(node):
            if not node: return 0
            a, b = DFS(node.left), DFS(node.right)
            self.ans += abs(a) + abs(b)
            return node.val + a + b - 1
        DFS(root)
        return self.ans
