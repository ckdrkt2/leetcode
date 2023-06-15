from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        stack, a = [(root,1)], {}
        while stack:
            node, level = stack.pop(0)
            if node:
                if level in a: a[level] += node.val
                else: a[level] = node.val
                stack.append((node.left, level+1))
                stack.append((node.right, level+1))
        return sorted(a.keys(), key=lambda x : a[x], reverse=True)[0]
