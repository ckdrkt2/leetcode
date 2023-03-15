from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        queue, is_end = deque([root]), False
        while queue:
            node = queue.popleft()
            if not node: is_end = True
            else:
                if is_end: return False
                queue.append(node.left)
                queue.append(node.right)
        return True