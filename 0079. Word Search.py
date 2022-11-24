class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n, length = len(board), len(board[0]), len(word)
        def dfs(i, j, cnt):
            if cnt == length - 1: return True
            tmp = board[i][j]
            board[i][j] = ''
            res = False
            for x, y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if not (0 <= x < m and 0 <= y < n): continue
                if board[x][y] == word[cnt+1]:
                    res |= dfs(x, y, cnt+1)
            board[i][j] = tmp
            return res
        ans = False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    ans |= dfs(i, j, 0)
        return ans