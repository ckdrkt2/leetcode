# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        answer = []
        stack = deque([(root, root.val, [root.val])])
        while stack:
            node, total, seen = stack.popleft()

            if node.left:
                stack.append((node.left, total + node.left.val, seen + [node.left.val]))
            if node.right:
                stack.append((node.right, total + node.right.val, seen + [node.right.val]))

            if not (node.left or node.right) and total == targetSum: answer.append(seen)
        return answer
