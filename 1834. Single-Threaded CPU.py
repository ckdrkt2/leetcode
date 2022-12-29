from heapq import heappop, heappush
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)): tasks[i].append(i)
        tasks.sort()
        time = tasks[0][0]
        heap, ans = [], []
        i = 0
        while heap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heappush(heap, tasks[i][1:])
                i += 1
            if heap:
                ptime, idx = heappop(heap)
                ans.append(idx)
                time += ptime
            else:
                time = tasks[i][0]
        return ans