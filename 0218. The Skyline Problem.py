from heapq import heappop, heappush
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        lst = sorted([(L, -H, R) for L, R, H in buildings] + [(R, 0, 0) for _, R, _ in buildings])
        ans = [[0,0]]; heap = [(0,float('inf'))]
        for L, H, R in lst:
            while L >= heap[0][1]:
                heappop(heap)
            if H < 0: heappush(heap, (H, R))
            max_height = -heap[0][0]
            if ans[-1][1] != max_height: ans.append([L,max_height])
        return ans[1:]