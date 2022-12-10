# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0
            total = dfs(node.left) + dfs(node.right) + node.val
            res.append(total)
            return total
        res = []
        s = dfs(root)
        return max(x * (s - x) for x in res) % 1000000007