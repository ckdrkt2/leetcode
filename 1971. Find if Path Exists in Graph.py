class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        q = [start]
        visit.add(start)
        while q != []:
            node = q.pop(0)
            if node == end: return True

            for i in adj[node]:
                if i not in visit:
                    q.append(i)
                    visit.add(i)
        return False