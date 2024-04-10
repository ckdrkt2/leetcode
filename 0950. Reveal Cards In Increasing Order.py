from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        index, ans = [i for i in range(len(deck))], [0] * len(deck)
        for card in sorted(deck):
            ans[index.pop(0)] = card
            if index:
                index.append(index.pop(0))
        return ans
