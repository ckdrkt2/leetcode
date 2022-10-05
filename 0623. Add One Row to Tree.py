# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1: return TreeNode(val, root)
        stack = deque([root])
        for _ in range(depth - 2):
            for _ in range(len(stack)):
                node = stack.popleft()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        for node in stack:
            left, right = node.left, node.right
            node.left = TreeNode(val, left)
            node.right = TreeNode(val, right=right)
        return root