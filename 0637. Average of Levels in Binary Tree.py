# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        stack, ans = [root], []
        while stack:
            s, c = 0, 0
            for _ in range(len(stack)):
                node = stack.pop(0)
                s += node.val
                c += 1
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
            ans.append(s/c)
        return ans