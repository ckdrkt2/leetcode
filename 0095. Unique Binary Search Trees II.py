from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def allPossibleBST(self, start, end, memo):
        ans = []
        if start > end:
            ans.append(None)
            return ans

        if (start, end) in memo:
            return memo[(start, end)]

        for i in range(start, end + 1):
            leftSubTree = self.allPossibleBST(start, i - 1, memo)
            rightSubTree = self.allPossibleBST(i + 1, end, memo)

            for left in leftSubTree:
                for right in rightSubTree:
                    root = TreeNode(i, left, right)
                    ans.append(root)

        memo[(start, end)] = ans
        return ans

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        return self.allPossibleBST(1, n, memo)
