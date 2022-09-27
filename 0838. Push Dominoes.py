class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n, stack, ans = len(dominoes), [0], ''
        for d in dominoes:
            if d == '.':
                if stack[-1] > 0: stack.append(stack[-1] - 1)
                else: stack.append(0)
            elif d == 'L':
                for i in range(len(stack)):
                    if abs(stack[-i-1]) != n:
                        stack[-i-1] -= n - i - 1
                    else: break
                stack.append(-n)
            else:
                stack.append(n)
        for num in stack[1:]:
            if num > 0: ans += 'R'
            elif num < 0: ans += 'L'
            else: ans += '.'
        return ans