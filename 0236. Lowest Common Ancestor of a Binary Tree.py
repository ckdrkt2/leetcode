# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            
            if node == p or node == q: return node
            
            if node is None: return node
            
            a = dfs(node.left)
            b = dfs(node.right)
            
            if a and b: return node
            else: return a or b
            
        return dfs(root)
