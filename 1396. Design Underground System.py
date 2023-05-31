class UndergroundSystem:

    def __init__(self):
        self.checks = {}
        self.history = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checks[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if (self.checks[id][0], stationName) in self.history:
            self.history[(self.checks[id][0], stationName)][0] += 1
            self.history[(self.checks[id][0], stationName)][1] += t - self.checks[id][1]
        else:
            self.history[(self.checks[id][0], stationName)] = [1, t - self.checks[id][1]]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.history[(startStation, endStation)][1] / self.history[(startStation, endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)