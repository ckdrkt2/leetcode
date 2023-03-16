from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: idx for idx, val in enumerate(inorder)}

        def build_helper(inorder_start, inorder_end, postorder_start, postorder_end):
            if inorder_start > inorder_end: return

            root_val = postorder[postorder_end]
            root = TreeNode(root_val)

            inorder_idx = idx_map[root_val]

            left_subtree_size = inorder_idx - inorder_start
            root.left = build_helper(inorder_start, inorder_idx - 1, postorder_start, postorder_start + left_subtree_size - 1)
            root.right = build_helper(inorder_idx + 1, inorder_end, postorder_start + left_subtree_size, postorder_end - 1)

            return root

        return build_helper(0, len(inorder) - 1, 0, len(postorder) - 1)
