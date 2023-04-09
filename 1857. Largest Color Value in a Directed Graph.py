from typing import List
from collections import defaultdict, Counter
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        tree = defaultdict(set)
        for a, b in edges: tree[a].add(b)
        status = [0] * len(colors)
        node = defaultdict(lambda: Counter())
        def dfs(idx):
            if status[idx] == -1:
                return None
            if status[idx] == 1:
                return node[idx]
            status[idx] = -1
            for c in tree[idx]:
                cur = dfs(c)
                if not cur:
                    return None
                for k in cur:
                    node[idx][k] = max(node[idx][k], cur[k])
            node[idx][colors[idx]] += 1
            status[idx] = 1
            return node[idx]
        ans = 0
        for i in range(len(colors)):
            cur = dfs(i)
            if not cur: return -1
            ans = max(ans, max(cur.values()))
        return ans
