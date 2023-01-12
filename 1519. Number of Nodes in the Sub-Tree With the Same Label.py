from collections import Counter, defaultdict
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(node: int, parent: int) -> Counter:
            c = Counter(labels[node])
            for child in graph.get(node, []):
                if child != parent:
                    c += dfs(child, node)
            ans[node] = c[labels[node]]
            return c

        graph, ans = defaultdict(list), [0] * n
        for a, b in edges:
            graph[a] += [b]
            graph[b] += [a]
        dfs(0, -1)
        return ans