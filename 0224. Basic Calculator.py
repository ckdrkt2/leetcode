class Solution:
    def calculate(self, s: str) -> int:
        stack, sign = [], 1
        num = res = 0
        for c in s:
            if c == ' ': continue
            elif c in ("-", "+"):
                res = res + num * sign
                num = 0
                sign = 1 if c =='+' else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif c == ")":
                res += sign * num
                res *= stack.pop()
                res += stack.pop()
                num = 0
            else: num = num * 10 + int(c)
        return res + num * sign