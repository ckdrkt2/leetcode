# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, m, M):
            if not node: return 0
            a, b, v = min(m, node.val), max(M, node.val), node.val
            return max(dfs(node.left, a, b), dfs(node.right, a, b), abs(m - v), abs(M - v))
        return dfs(root, root.val, root.val)