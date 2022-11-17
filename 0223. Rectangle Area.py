class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        left, right, top, bot = max(bx1, ax1), min(bx2, ax2), min(ay2, by2), max(by1, ay1)
        return (ay2 - ay1) * (ax2 - ax1) + (by2 - by1) * (bx2 - bx1) - max(0, top - bot) * max(0, right - left)