# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def DFS(current):
            if not current:
                return 0
            a, b, = DFS(current.left),  DFS(current.right)
            if not a:
                current.left = None
            if not b:
                current.right = None
            return current.val or a or b
        DFS(root)
        if not root.val and not root.left and not root.right: return None
        return root