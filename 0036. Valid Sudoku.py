from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        check = defaultdict(dict)
        for i in range(1, 10):
            c = str(i)
            check[c]['row'] = [0] * 9
            check[c]['col'] = [0] * 9
            check[c]['box'] = [0] * 9
        for i, cells in enumerate(board):
            for j, cell in enumerate(cells):
                if cell == '.': continue
                box = 3 * (i // 3) + (j // 3)
                if check[cell]['row'][i-1] or check[cell]['col'][j-1] or check[cell]['box'][box]: return False
                check[cell]['row'][i-1] = 1
                check[cell]['col'][j-1] = 1
                check[cell]['box'][box] = 1
        return True