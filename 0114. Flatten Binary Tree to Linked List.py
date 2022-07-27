# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.head = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def preorder(root):
            if not root: return

            preorder(root.right)
            preorder(root.left)

            root.left = None
            root.right = self.head
            self.head = root

        preorder(root)