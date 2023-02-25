from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, ans = 10000, 0
        for price in prices:
            if price - min_price < 0:
                min_price = price
            elif price - min_price > 0 and price - min_price > ans:
                profit = price - min_price
        return ans