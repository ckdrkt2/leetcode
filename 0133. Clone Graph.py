# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None: return None
        def DFS(node, visited):
            if node not in visited:
                a = Node(node.val)
                visited[node] = a
                for i in node.neighbors:
                    a.neighbors.append(DFS(i, visited))
            return visited[node]
        return DFS(node, {})