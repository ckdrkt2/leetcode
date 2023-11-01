from typing import Optional, List, Dict
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node: Optional[TreeNode], counter: Dict):
            if not node: return

            counter[node.val] += 1
            dfs(node.left, counter)
            dfs(node.right, counter)

        counter = defaultdict(int)
        dfs(root, counter)
        max_freq = max(counter.values())

        return [key for key in counter if counter[key] == max_freq]
