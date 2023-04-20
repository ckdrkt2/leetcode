from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q, ans = deque([(root, 0)]), 0
        while q:
            l = len(q)
            w = 1 if l == 1 else q[-1][1] - q[0][1] + 1
            ans = max(ans, w)
            for _ in range(l):
                node, n = q.popleft()
                if node.left:
                    q.append((node.left, 2 * n + 1))
                if node.right:
                    q.append((node.right, 2 * n + 2))
        return ans
