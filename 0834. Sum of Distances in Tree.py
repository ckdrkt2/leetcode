from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for a, b in edges:
            d[a].append(b)
            d[b].append(a)

        ans, count = [0] * n, [0] * n

        def dfs(root, prev):
            for i in d[root]:
                if i == prev: continue
                dfs(i, root)
                count[root] += count[i]
                ans[root] += ans[i] + count[i]
            count[root] += 1

        def dfs2(root, prev):
            for i in d[root]:
                if i == prev: continue
                ans[i] = ans[root] - count[i] + len(count) - count[i]
                dfs2(i, root)

        dfs(0, -1)
        dfs2(0, -1)
        return ans