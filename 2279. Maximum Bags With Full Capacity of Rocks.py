from heapq import heappop, heappush
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        ans, heap = 0, []
        for c, r in zip(capacity, rocks):
            if c == r:
                ans += 1
            else:
                heappush(heap, c - r)
        while heap:
            cap = heappop(heap)
            if cap > additionalRocks: break
            additionalRocks -= cap
            ans += 1
        return ans