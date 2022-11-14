from collections import defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        seen = set()
        rows, cols = defaultdict(list), defaultdict(list)
        for x, y in stones:
            rows[x].append(y)
            cols[y].append(x)
        def dfs(row):
            seen.add(row)
            for col in rows[row]:
                for nxt in cols[col]:
                    if nxt not in seen: dfs(nxt)
        ans = 0
        for row in rows:
            if row not in seen:
                dfs(row)
                ans += 1
        return len(stones) - ans