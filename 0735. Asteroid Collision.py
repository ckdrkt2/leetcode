from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and 0 < stack[-1] < abs(asteroid):
                    stack.pop()

                if stack and stack[-1] == abs(asteroid):
                    stack.pop()
                else:
                    if not stack or stack[-1] < 0:
                        stack.append(asteroid)
        return stack
