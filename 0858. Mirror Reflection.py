class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        x = 1
        while p * x % q: x += 1

        if x % 2: return 1 if (p * x // q) % 2 else 2

        return 0