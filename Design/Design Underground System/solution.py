class UndergroundSystem:

    def __init__(self):
        self.t = defaultdict(dict)
        self.check_in = dict()

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        from_station, start = self.check_in.pop(id)
        to_station = stationName
        if to_station not in self.avg[from_station]:
            self.avg[from_station][to_station] = [0, 0]
        self.avg[from_station][to_station][0] += t - start
        self.avg[from_station][to_station][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.avg[startStation][endStation][0] / self.avg[startStation][endStation][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)