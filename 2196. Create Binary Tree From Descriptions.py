from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        data, children = dict(), set()
        for parent, child, isLeft in descriptions:
            children.add(child)
            if parent not in data:
                data[parent] = TreeNode(parent)
            if child not in data:
                data[child] = TreeNode(child)
            if isLeft:
                data[parent].left = data[child]
            else:
                data[parent].right = data[child]

        root = (set(data.keys()) - children).pop()
        return data[root]
