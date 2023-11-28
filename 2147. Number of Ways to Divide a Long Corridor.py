class Solution:
    def numberOfWays(self, corridor: str) -> int:
        if corridor.count('S') % 2: return 0
        seat = plant = 0
        ans = 1
        for c in corridor:
            if c == 'S':
                if seat == 2:
                    ans *= plant + 1 if plant else 1
                    plant, s = 0, 1
                else:
                    seat += 1
            else:
                plant += int(seat == 2)
        return ans % 1000000007
