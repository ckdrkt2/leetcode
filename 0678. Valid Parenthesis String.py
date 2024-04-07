class Solution:
    def checkValidString(self, s: str) -> bool:
        lower = upper = 0
        for c in s:
            if c == '(':
                lower += 1
                upper += 1
            elif c == ')':
                lower = max(0, lower - 1)
                upper -= 1
                if upper < 0:
                    return False
            else:
                lower = max(0, lower - 1)
                upper += 1

        return lower == 0
