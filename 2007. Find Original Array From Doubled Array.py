class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ans, stack = [], []
        for n in sorted(changed):
            if not stack:
                stack.append(n)
            elif n % 2:
                stack.append(n)
            elif n // 2 != stack[0]:
                stack.append(n)
            else:
                ans.append(stack.pop(0))
        return [] if stack else ans