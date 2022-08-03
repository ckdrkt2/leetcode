from bisect import bisect_left, bisect_right
class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start, end) -> bool:
        if end <= start: return False

        i = bisect_right(self.calendar, start)
        if i % 2: return False

        j = bisect_left(self.calendar, end)
        if i != j: return False

        self.calendar[i:i] = [start, end]
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)