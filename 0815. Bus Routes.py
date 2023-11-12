from typing import List
from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        buses = defaultdict(set)
        for bus, route in enumerate(routes):
            for stop in route:
                buses[stop].add(bus)

        q = deque([source])
        ans, seen = 0, set()

        while q:
            for _ in range(len(q)):
                cur = q.popleft()

                if cur == target:
                    return ans

                for bus in buses[cur]:
                    if bus in seen: continue
                    seen.add(bus)
                    for stop in routes[bus]:
                        if cur == stop: continue
                        q.append(stop)
            ans += 1

        return -1
