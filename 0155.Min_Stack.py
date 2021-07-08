class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        small = self.min[-1] if self.min else 2**31-1
        if x <= small:
            self.min.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()