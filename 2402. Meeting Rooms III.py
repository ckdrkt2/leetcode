from typing import List
from heapq import heappop, heappush


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meetings.sort()
        cnt, busy, available = [0] * n, [], [i for i in range(n)]

        for start, end in meetings:
            while busy and busy[0][0] <= start:
                _, room = heappop(busy)
                heappush(available, room)

            if not available:
                prev, room = heappop(busy)
                heappush(busy, (end - start + prev, room))
            else:
                room = heappop(available)
                heappush(busy, (end, room))

            cnt[room] += 1

        return cnt.index(max(cnt))
