from typing import Optional
from collection import ascii_lowercase

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = "z" * 15
        stack = [(root, ascii_lowercase[root.val])]
        while stack:
            cur, val = stack.pop()
            if (cur.left is None and cur.right is None):
                ans = min(ans, val)
            if cur.left:
                stack.append((cur.left, ascii_lowercase[cur.left.val] + val))
            if cur.right:
                stack.append((cur.right, ascii_lowercase[cur.right.val] + val))
        return ans
