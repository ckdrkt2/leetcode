# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def search(node, path, depth):
            for p in bin(path)[2:].zfill(depth-1):
                if p == '0': node = node.left
                else: node = node.right
            return node
        if not root: return 0
        left, depth = root, 0
        while left:
            left = left.left
            depth += 1
        if depth == 1: return 1
        l, r = 0, 2**(depth-1)-1
        if search(root, r, depth): return 2**depth - 1
        while l <= r:
            m = (l + r) // 2
            if search(root, m, depth):
                l = m + 1
            else:
                r = m - 1
        return 2**(depth-1) + r