from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(i, j, 0, board, word):
                        return True
        return False

    def dfs(self, i: int, j: int, cnt: int, board: List[List[str]], word: str) -> bool:
        if cnt == len(word) - 1: return True

        tmp, res = board[i][j], False
        board[i][j] = ''
        for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
            if not (0 <= x < len(board) and 0 <= y < len(board[0])):
                continue
            if board[x][y] == word[cnt + 1]:
                res |= self.dfs(x, y, cnt + 1, board, word)
        board[i][j] = tmp
        return res
