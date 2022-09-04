from collections import defaultdict
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        d_row = {}
        stack = [(root, 0, 0)]
        while stack:
            node, row, col = stack.pop(0)
            d[col].append(node.val)
            d_row[node.val] = row
            if node.left: stack.append((node.left, row + 1, col - 1))
            if node.right: stack.append((node.right, row + 1, col + 1))
        ans = []
        for col in sorted(d.keys()):
            ans.append(sorted(d[col], key = lambda x : (d_row[x], x)))
        return ans