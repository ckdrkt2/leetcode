class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1 or n == 2 or n == 3:
            return False
        elif n == 1: return True
        while n > 1 :
            if n % 4 != 0:
                return False
            n = n // 4
        return True