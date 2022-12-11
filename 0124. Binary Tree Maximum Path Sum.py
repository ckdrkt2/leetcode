# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float("-inf")
        def dfs(node):
            if not node: return 0
            v0, v1, v2 = node.val, dfs(node.left), dfs(node.right)
            self.ans = max(v0 + v1 + v2, self.ans, v0, v0 + v1, v0 + v2)
            return max(max(v1, v2) + v0, v0, v0 + v1, v0 + v2)
        dfs(root)
        return self.ans