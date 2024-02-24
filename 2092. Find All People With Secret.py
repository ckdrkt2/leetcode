from typing import List
from collections import deque, defaultdict
from itertools import groupby


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        known = {0, firstPerson}
        for _, meeting in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]):
            queue = set()
            graph = defaultdict(list)
            for x, y, _ in meeting:
                graph[x].append(y)
                graph[y].append(x)
                if x in known: queue.add(x)
                if y in known: queue.add(y)

            queue = deque(queue)
            while queue:
                x = queue.popleft()
                for y in graph[x]:
                    if y not in known:
                        known.add(y)
                        queue.append(y)
        return list(known)
