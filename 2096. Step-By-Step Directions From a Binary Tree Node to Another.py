from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: TreeNode, startValue: int, destValue: int) -> str:
        startPath, destPath = [], []
        self.dfs(root, startValue, startPath)
        self.dfs(root, destValue, destPath)

        while startPath and destPath and startPath[-1] == destPath[-1]:
            startPath.pop()
            destPath.pop()
        return "U" * len(startPath) + "".join(destPath[::-1])

    def dfs(self, node: TreeNode, target: int, path: List[str]) -> bool:
        if node.val == target:
            return True
        if node.left and self.dfs(node.left, target, path):
            path += "L"
        elif node.right and self.dfs(node.right, target, path):
            path += "R"
        return len(path) > 0
