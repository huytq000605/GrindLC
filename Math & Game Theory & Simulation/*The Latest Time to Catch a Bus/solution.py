class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        n = len(buses)
        buses.sort()
        passengers.sort()
        j = 0
        result = 0
        for i in range(n):
            time = buses[i]
            cap = capacity
            while cap > 0 and j < len(passengers) and passengers[j] <= time:
                j += 1
                cap -= 1

            # On the last trip
            # If we can still handle more passengers, then the latest will be at the departure time
            # Otherwise, it will be the latest passenger
            if i == n-1:
                if cap > 0:
                    result = buses[-1]
                else:
                    result = passengers[j-1]

        passengers_set = set(passengers)
        while result in passengers_set:
            result -= 1
        return result
