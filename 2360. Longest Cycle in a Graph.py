from typing import List
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        time = [0] * len(edges)
        clock, ans = 1, -1
        for x, t in enumerate(time):
            if t:
                continue
            start_time = clock
            while x >= 0:
                if time[x]:
                    if time[x] >= start_time:
                        ans = max(ans, clock - time[x])
                    break
                time[x] = clock
                clock += 1
                x = edges[x]
        return ans
