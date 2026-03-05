class UndergroundSystem:

    def __init__(self):
        self.check_in_map = {}
        self.travel_stats = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_map[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in_map.pop(id)
        
        duration = t - start_time
        route = (start_station, stationName)
        
        if route not in self.travel_stats:
            self.travel_stats[route] = [0, 0]
        
        self.travel_stats[route][0] += duration
        self.travel_stats[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # Retrieve total time and count to return the average
        total_time, count = self.travel_stats[(startStation, endStation)]
        return total_time / count