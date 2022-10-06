from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.tmap[key]
        if vals and timestamp >= vals[-1][1]:
            return vals[-1][0]

        l, r = 0, len(vals) - 1
        while l <= r:
            m = (l + r) // 2
            if vals[m][1] <= timestamp:
                l = m + 1
            else:
                r = m - 1
        return vals[r][0] if r >= 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)