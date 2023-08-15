# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        a = [root]; s = 0
        while a:
            n = a.pop()
            if n:
                v = n.val
                if v > low:
                    a.append(n.left)
                if v < high:
                    a.append(n.right)
                if low <= v <= high:
                    s += n.val
        return s