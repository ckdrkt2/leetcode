class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        s, banned = set(), [False] * len(senate)
        ban_d = ban_r = 0
        while len(s) != 1:
            s = set()
            for i, p in enumerate(senate):
                if banned[i]: continue
                if p == 'R':
                    if ban_r > 0:
                        ban_r -= 1
                        banned[i] = True
                    else:
                        ban_d += 1
                        s.add('R')
                else:
                    if ban_d > 0:
                        ban_d -= 1
                        banned[i] = True
                    else:
                        ban_r += 1
                        s.add('D')
        return 'Radiant' if s.pop() == 'R' else 'Dire'
