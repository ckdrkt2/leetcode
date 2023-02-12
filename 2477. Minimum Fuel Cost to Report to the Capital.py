from typing import List
from collections import defaultdict
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        if not roads: return 0
        self.ans, self.visited = 0, set([0])
        d = defaultdict(list)
        for a, b in roads:
            d[a].append(b)
            d[b].append(a)
        def dfs(city):
            self.visited.add(city)
            reps = 1
            for c in d[city]:
                if c in self.visited: continue
                reps += dfs(c)
            self.ans += (reps // seats) + -(-(reps % seats) // seats)
            return reps
        for city in d[0]: dfs(city)
        return self.ans