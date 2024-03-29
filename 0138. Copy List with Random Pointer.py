
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None: return None
        a, b = [Node(0)], [head]
        while True:
            a[-1].val = b[-1].val
            if b[-1].next is None: break
            a[-1].next = Node(0)
            a.append(a[-1].next)
            b.append(b[-1].next)
        for i, node in enumerate(b):
            a[i].random = None if node.random is None else a[b.index(node.random)]
        return a[0]
