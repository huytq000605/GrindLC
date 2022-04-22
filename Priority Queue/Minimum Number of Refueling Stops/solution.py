class Solution:
    def minRefuelStops(self, target: int, fuel: int, stations: List[List[int]]) -> int:
        i, j = 0, 0
        stop = []
        result = 0
        while i < target:
            if fuel > 0:
                i += fuel
                fuel = 0
            else:
                while j < len(stations) and i >= stations[j][0]:
                    heappush(stop, -stations[j][1])
                    j += 1
                if len(stop) == 0:
                    return -1
                fuel += (-heappop(stop))
                result += 1
        return result