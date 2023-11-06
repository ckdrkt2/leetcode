from heapq import heappush, heappop
class SeatManager:

    def __init__(self, n: int):
        self.seats = 0
        self.unreserved = []

    def reserve(self) -> int:
        if not self.unreserved:
            self.seats += 1
            return self.seats

        return heappop(self.unreserved)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.unreserved, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)