# 브루트 포스를 사용하지 않고 구현
# 최저 값이 바뀌기 전까지 최대 수익 저장
# 최저가 바뀐 후에 최대 수익이 바뀌지 않을 때를 해결
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10000; profit = 0
        for price in prices:
            if price - min_price < 0:
                min_price = price
            elif price - min_price > 0 and price - min_price > profit:
                profit = price - min_price
        return profit