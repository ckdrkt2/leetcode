class Solution:
    def numSteps(self, s: str) -> int:
        steps = carry = 0
        for n in s[:0:-1]:
            if int(n) + carry == 1:
                carry = 1
                steps += 1
            steps += 1
        return steps + carry
