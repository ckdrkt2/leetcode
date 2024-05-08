from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        medal = lambda x : ("Gold Medal", "Silver Medal", "Bronze Medal")[x] if x < 3 else str(x + 1)
        ranks = sorted([i for i in range(len(score))], key=lambda x : score[x], reverse=True)
        return [medal(ranks.index(i)) for i in range(len(score))]
