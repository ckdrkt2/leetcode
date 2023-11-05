from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        cur, win = arr[0], 0

        for i in range(1, len(arr)):
            if cur < arr[i]:
                cur, win = arr[i], 0

            win += 1
            if win == k: return cur
        return cur
