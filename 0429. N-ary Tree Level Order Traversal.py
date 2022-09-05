"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        stack = [root]
        a = []
        while stack:
            l = len(stack)
            b = []
            for i in range(l):
                node = stack.pop(0)
                b.append(node.val)
                for c in node.children:
                    if c: stack.append(c)
            a.append(b)
        return a
