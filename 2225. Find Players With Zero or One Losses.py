from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        zero, one, two = set(), set(), set()

        for winner, loser in matches:
            if (winner not in one) and (winner not in two):
                zero.add(winner)

            if loser in zero:
                zero.remove(loser)
                one.add(loser)
            elif loser in one:
                one.remove(loser)
                two.add(loser)
            elif loser in two:
                continue
            else:
                one.add(loser)

        return [sorted(zero), sorted(one)]
