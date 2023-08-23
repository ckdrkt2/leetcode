from collections import Counter
from heapq import heappop, heappush, heapify
class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = ""
        heap = [(-count, char) for char, count in Counter(s).items()]
        heapify(heap)
        while heap:
            count1, char1 = heappop(heap)
            if not ans or char1 != ans[-1]:
                ans += char1
                if count1 < -1: heappush(heap, (count1 + 1, char1))
            else:
                if not heap: return ""
                count2, char2 = heappop(heap)
                ans += char2
                if count2 < -1: heappush(heap, (count2 + 1, char2))
                heappush(heap, (count1, char1))
        return ans








