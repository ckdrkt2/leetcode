from typing import List
from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        q = deque([root])
        while q:
            node = q.popleft()

            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                q.append(node.left)

            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                q.append(node.right)

        q.append(target.val)
        seen = set()
        for _ in range(k):
            for _ in range(len(q)):
                cur = q.popleft()
                seen.add(cur)
                for n in graph[cur]:
                    if n in seen: continue
                    q.append(n)

        return list(q)
