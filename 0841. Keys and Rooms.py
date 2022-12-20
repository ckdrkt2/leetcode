class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(i):
            if i not in visit:
                visit.add(i)
                for room in rooms[i]: dfs(room)
        visit = set()
        dfs(0)
        return len(visit) == len(rooms)