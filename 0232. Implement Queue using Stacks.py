class MyQueue:

    def __init__(self):
        self.input_s = []
        self.output_s = []

    def push(self, x: int) -> None:
        self.input_s.append(x)

    def pop(self) -> int:
        self.rearrange()
        return self.output_s.pop()

    def peek(self) -> int:
        self.rearrange()
        return self.output_s[-1]

    def empty(self) -> bool:
        return not self.output_s and not self.input_s

    def rearrange(self):
        if self.output_s: return

        while self.input_s:
            self.output_s.append(self.input_s.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()