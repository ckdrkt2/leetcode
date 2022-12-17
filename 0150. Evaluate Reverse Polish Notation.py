class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ('+','-','*','/'):
                stack.append(token)
                continue
            b, a = stack.pop(), stack.pop()
            stack.append(str(int(eval(a + token + b))))
        return int(stack[-1])
