class StockSpanner:

    def __init__(self):
        self.stack = [(100001,0)]
    def next(self, price: int) -> int:
        c = 1
        while self.stack[-1][0] <= price:
            c += self.stack.pop()[1]
        self.stack.append((price, c))
        return c

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)