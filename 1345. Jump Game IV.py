from typing import List
from collections import deque, defaultdict
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n, d = len(arr), defaultdict(set)
        for i, a in enumerate(arr): d[a].add(i)
        q, seen, seenum = deque([(0, 0)]), set((-1, 0)), set()
        while q:
            idx, jumps = q.popleft()
            if idx == n - 1: return jumps
            for i in [idx - 1, idx + 1]:
                if i in seen: continue
                q.append((i, jumps + 1))
                seen.add(i)
            if arr[idx] in seenum: continue
            for i in d[arr[idx]] - seen:
                if i in seen: continue
                q.append((i, jumps + 1))
                seen.add(i)
            seenum.add(arr[idx])
        return -1 # for debug