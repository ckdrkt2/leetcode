class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack):
                    a = stack.pop() + i
                else:
                    a = i
                if a == '()' or a =='{}' or a =='[]':
                    continue
                else:
                    return False
        return False if stack else True
