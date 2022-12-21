class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if n == 1 or not dislikes:
            return True

        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        seen = {}
        for i in range(n):
            if i not in seen and not self.helper(i, 1, seen, graph):
                return False
        return True

    def helper(self, i, color, seen, graph):
        if i in seen:
            return seen[i] == color

        seen[i] = color
        for nb in graph[i]:
            if not self.helper(nb, -color, seen, graph):
                return False
        return True