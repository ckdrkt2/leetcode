class Solution:
    def reverse(self, x: int) -> int:
        a = list(str(x))
        if a[0] == '-':
            a.remove('-')
            a.append('-')
        a.reverse()
        answer = int(''.join(a))
        if answer > 2**31 - 1 or answer < -2**31:
            return 0
        return answer
            