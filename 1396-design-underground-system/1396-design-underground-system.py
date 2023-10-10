class UndergroundSystem:

    def __init__(self):
        self.checkins = {}
        
        self.total_duration = defaultdict(int)
        self.total_count = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkins[id] = (stationName, t)        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.checkins[id]
        
        duration = t - start_time
        
        self.total_duration[(start_station, stationName)] += duration
        self.total_count[(start_station, stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel = (startStation, endStation)
        return self.total_duration[travel] / self.total_count[travel]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)