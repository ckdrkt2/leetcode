class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if not poured: return 0
        if not query_row: return 1
        
        ex = [poured]
        for row in range(1,query_row+1):
            cur = [0] * (row + 1)
            for i in range(len(ex)):
                rest = ex[i] - 1
                if rest < 0: continue
                cur[i] += rest / 2
                cur[i+1] += rest / 2
            ex = cur
        return min(cur[query_glass], 1)
