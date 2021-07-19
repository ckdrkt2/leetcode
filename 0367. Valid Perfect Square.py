class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num**0.5 == int(num**0.5):
            return True
        else:
            return False