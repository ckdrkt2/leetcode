class SummaryRanges:
    def __init__(self):
        self.seen = set()

    def addNum(self, val: int) -> None:
        self.seen.add(val)

    def getIntervals(self) -> List[List[int]]:
        ans = []
        for v in sorted(self.seen):
            if not ans or v > ans[-1][1] + 1:
                ans.append([v, v])
            elif ans and v == ans[-1][1] + 1:
                ans[-1][1] = v
        return ans