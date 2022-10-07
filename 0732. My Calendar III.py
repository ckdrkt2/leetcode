from bisect import bisect_left, bisect_right
class MyCalendarThree:

    def __init__(self):
        self.starts = []
        self.ends = []
        self.k = 0
        
    def book(self, start: int, end: int) -> int:
        left = bisect.bisect_left(self.ends, start)
        right = bisect.bisect_right(self.starts, end)
        
        bisect.insort_left(self.starts, start)
        bisect.insort_left(self.ends, end)
        
        hq = []
        for i in range(left, right + 1):
            while hq and hq[0] <= self.starts[i]:
                hq.pop(0)
            
            hq.append(self.ends[i])
            self.k = max(self.k, len(hq))
            
        return self.k


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)
