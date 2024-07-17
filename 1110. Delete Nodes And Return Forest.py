from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.ans = []
        self.dfs(root, to_delete)
        if root.val != -1:
            self.ans.append(root)
        return self.ans

    def dfs(self, node, to_delete):
        if node is None: return
        self.dfs(node.left, to_delete)
        self.dfs(node.right, to_delete)

        node.val = -1 if node.val in to_delete else node.val

        if node.left:
            if node.left.val == -1:
                node.left = None
            elif node.val == -1:
                self.ans.append(node.left)
        if node.right:
            if node.right.val == -1:
                node.right = None
            elif node.val == -1:
                self.ans.append(node.right)
