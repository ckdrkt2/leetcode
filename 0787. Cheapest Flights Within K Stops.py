from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        d = defaultdict(dict)
        check = False
        for a, b, p in flights:
            d[a][b], check = p, check | (dst == b)
        if not check: return -1

        heap = [(0, 0, src, [])]
        while heap:
            prices, stops, cur, seen = heappop(heap)
            if stops > k + 1: continue
            if cur == dst: return prices
            for city in d[cur]:
                if city in seen: continue
                heappush(heap, (prices + d[cur][city], stops + 1, city, seen + [cur]))
        return -1