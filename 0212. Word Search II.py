class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        search = {}
        for word in words:
            cur = search
            for w in word:
                if w not in cur: cur[w] = {}
                cur = cur[w]
            cur["$"] = word
        def dfs(i, j, trie):
            c = board[i][j]
            if "$" in trie[c]:
                ans.append(trie[c]["$"])
                del trie[c]["$"]
            board[i][j] = ''
            for x, y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if not (0 <= x < m and 0 <= y < n): continue
                if board[x][y] not in trie[c]: continue
                dfs(x, y, trie[c])
            board[i][j] = c
            if not trie[c]: trie.pop(c)
            return
        ans = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in search: dfs(i, j, search)
        return ans