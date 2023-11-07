from typing import List
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival = []
        for i in range(len(dist)):
            arrival.append(dist[i] / speed[i])

        arrival.sort()
        ans = 0

        for i, arr in enumerate(arrival):
            if arr <= i: break
            ans += 1

        return ans