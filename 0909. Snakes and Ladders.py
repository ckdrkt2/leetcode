from collections import deque
class Solution:
    def snakesAndLadders(self, board):
        return self.bfs(board)

    def bfs(self, board):
        N, level = len(board), 0

        line = [0]
        for row in range(N)[::-1]:
            line.extend(board[row] if (N - row) % 2 else board[row][::-1])

        queue, visit, target = deque([1]), set(), N * N
        next_options = lambda n: range(n + 1, min(n + 6, target) + 1)

        while queue:
            level += 1
            for _ in range(len(queue)):
                cur = queue.popleft()

                if cur in visit: continue
                visit.add(cur)

                for nxt in next_options(cur):
                    if line[nxt] != -1: nxt = line[nxt]
                    if nxt == target: return level
                    queue.append(nxt)
        return -1