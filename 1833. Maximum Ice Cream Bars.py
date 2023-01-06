class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        for i, n in enumerate(sorted(costs)):
            coins -= n
            if coins < 0: break
        return i + (coins > 0)