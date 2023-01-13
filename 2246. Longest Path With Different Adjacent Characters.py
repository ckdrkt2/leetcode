class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        for i in range(1,len(parent)):
            tree[parent[i]].append(i)
        self.ans = 1
        def dfs(v):
            if not tree[v]: return 1
            res = 1
            for w in tree[v]:
                children = dfs(w)
                if s[v] != s[w]:
                    self.ans = max(self.ans, children + res)
                    res = max(res, children + 1)
            return res
        dfs(0)
        return self.ans