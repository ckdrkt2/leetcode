from typing import List
from heapq import heappush, heappop


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap, n = [], len(heights)

        for i in range(n-1):
            h = heights[i+1] - heights[i]
            if h <= 0: continue

            heappush(heap, h)
            if len(heap) > ladders:
                min_height = heappop(heap)
                bricks -= min_height

            if bricks < 0: return i

        return n - 1
