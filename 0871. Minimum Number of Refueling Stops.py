from bisect import bisect_left
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        dp, fuel, ans, cur = [], startFuel, 0, 0
        for loc, cap in stations:
            fuel -= loc - cur
            while dp and fuel < 0:
                fuel += dp.pop()
                ans += 1
            if fuel < 0: return -1
            dp.insert(bisect_left(dp, cap), cap)
            cur = loc
        return ans
'''
DFS Solution -> Time Limit Exceeded
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if startFuel >= target: return 0
        std = {x[0]:x[1] for x in stations}
        def dfs(cur, fuel, cnt, lst):
            if target <= cur + fuel: return cnt
            m = 501
            for i, s in enumerate(lst):
                if cur < s <= cur + fuel:
                    m = min(m, dfs(s, std[s] + fuel - s + cur, cnt + 1, lst[i+1:]))
            return m
        ans = dfs(0, startFuel, 0, std.keys())
        return ans if ans < 501 else -1
'''