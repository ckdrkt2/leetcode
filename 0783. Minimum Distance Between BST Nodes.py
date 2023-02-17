class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans, self.pre = 100000, -100000

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        if root is None: return

        self.minDiffInBST(root.left)
        self.ans = min(self.ans, root.val - self.pre)
        self.pre = root.val
        self.minDiffInBST(root.right)

        return self.ans