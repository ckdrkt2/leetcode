# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root: return False
        stack, d = [root], set()
        while stack:
            node = stack.pop(0)
            if node.val in d: return True
            d.add(k - node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False