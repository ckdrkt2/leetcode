from collections import deque
class Solution:
    def removeStars(self, s: str) -> str:
        q = deque()
        for c in s:
            if c != "*":
                q.append(c)
            else:
                q.pop()
        return "".join(q)
