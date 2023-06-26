from typing import List
from heapq import heapify, heappop, heappush
class Solution:
    def totalCost(self, costs: List[int], k: int, n: int) -> int:
        leftheap = costs[:n]
        rightheap = costs[max(n, len(costs) - n):]
        heapify(leftheap)
        heapify(rightheap)
        ans = 0
        ln, rn = n, len(costs) - 1 - n
        for _ in range(k):
            if not rightheap or (leftheap and leftheap[0] <= rightheap[0]):
                ans += heappop(leftheap)
                if ln <= rn:
                    heappush(leftheap, costs[ln])
                    ln += 1
            else:
                ans += heappop(rightheap)
                if ln <= rn:
                    heappush(rightheap, costs[rn])
                    rn -= 1
        return ans
