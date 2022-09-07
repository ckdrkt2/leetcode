# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        left_side = "(" + self.tree2str(root.left) + ")"
        right_side = "(" + self.tree2str(root.right) + ")"
        
        ans = str(root.val)
        if root.left or root.right:
            ans += left_side
        if root.right:
            ans += right_side
        
        return ans
