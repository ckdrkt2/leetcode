from collections import deque
class Solution:
    def numSquares(self, n: int) -> int:
        square = [(i+1)**2 for i in range(int(n**0.5))]
        ans = float('inf')
        q = deque([(n,0)])
        while q:
            num, cnt = q.popleft()
            if cnt > ans: continue
            for s in square:
                if s > num: break
                if num % s == 0: ans = min(ans, cnt + (num // s))
                else: q.append((num % s, cnt + (num // s)))
        return ans