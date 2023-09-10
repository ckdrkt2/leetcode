class Solution:
    def countOrders(self, n: int) -> int:
        return n * (2 * n - 1) * self.countOrders(n - 1) % 1000000007 if n > 1 else 1
