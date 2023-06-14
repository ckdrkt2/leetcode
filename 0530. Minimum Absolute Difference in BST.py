# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root):
        def dfs(node, lst):
            if node.left: dfs(node.left, lst)
            lst.append(node.val)
            if node.right: dfs(node.right, lst)
            return lst
        ans = dfs(root, [])
        return min([abs(a - b) for a, b in zip(ans, ans[1:])])
