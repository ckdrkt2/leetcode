class BrowserHistory:

    def __init__(self, homepage: str):
        self.x = 0
        self.l = 1
        self.stack = [homepage]

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.x+1]
        self.x += 1
        self.stack.append(url)
        self.l = self.x + 1

    def back(self, steps: int) -> str:
        if steps > self.x: steps = self.x
        self.x = self.x - steps
        return self.stack[self.x]

    def forward(self, steps: int) -> str:
        self.x = self.x + steps
        if self.x >= self.l: self.x = self.l - 1
        return self.stack[self.x]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)