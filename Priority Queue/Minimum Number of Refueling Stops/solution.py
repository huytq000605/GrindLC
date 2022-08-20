class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.sort()
        pq = []
        result = 0
        station_idx = 0
        position = startFuel
        fuel = 0
        while position < target:
            while station_idx < len(stations) and position >= stations[station_idx][0]:
                heappush(pq, -stations[station_idx][1])
                station_idx += 1
            if not fuel:
                if pq:
                    result += 1
                    fuel += -heappop(pq)
                else:
                    return -1
            position += fuel
            fuel = 0
        return result
