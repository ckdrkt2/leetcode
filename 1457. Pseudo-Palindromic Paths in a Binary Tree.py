# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def DFS(node, lst):
            if not node: return 0
            lst ^= 1 << node.val
            if not node.left and not node.right:
                return 0 if bin(lst).count('1') > 1 else 1
            return DFS(node.left, lst) + DFS(node.right, lst)
        return DFS(root, 0)