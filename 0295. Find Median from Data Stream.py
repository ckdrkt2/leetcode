from heapq import heappush, heappushpop
class MedianFinder:

    def __init__(self):
        self.upper, self.lower = [], []
        self.usize = self.lsize = 0

    def addNum(self, num: int) -> None:
        if self.usize == self.lsize:
            heappush(self.lower, -heappushpop(self.upper, -num))
            self.lsize += 1
        else:
            heappush(self.upper, -heappushpop(self.lower, num))
            self.usize += 1

    def findMedian(self) -> float:
        if self.usize == self.lsize:
            return (self.lower[0] - self.upper[0]) / 2
        else:
            return self.lower[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()