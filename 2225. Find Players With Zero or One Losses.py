from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d, players = Counter(), set()
        ans = [[],[]]
        for winner, loser in matches:
            d[loser] += 1
            players.add(winner)
            players.add(loser)
        for player in sorted(players):
            cnt = d[player]
            if cnt == 0: ans[0].append(player)
            elif cnt == 1: ans[1].append(player)
        return ans