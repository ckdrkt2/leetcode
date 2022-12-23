class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a, b, c = 0, float('-inf'), float('-inf')
        for p in prices:
            c, a, b = max(c, a - p), max(a, b), c + p
        return max(a, b)