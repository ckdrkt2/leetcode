from typing import Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans, q = 0, deque([(root, 0, None)])
        while q:
            node, n, left = q.popleft()
            if node:
                ans = max(ans, n)
                q.append((node.left, 1 if left else n + 1, 1))
                q.append((node.right, n + 1 if left else 1, 0))
        return ans
