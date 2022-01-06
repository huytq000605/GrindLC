class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda trip: trip[1])
        arr = [0] * 1001
        for trip in trips:
            passengers, start, end = trip
            arr[start] += passengers
            arr[end] -= passengers
        passengers = 0
        for time in range(1001):
            passengers += arr[time]
            if passengers > capacity:
                return False
        return True
