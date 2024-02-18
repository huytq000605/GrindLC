from heapq import heapify, heappush, heappop

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        counter = [0 for _ in range(n)]
        free_rooms = [i for i in range(n)]
        heapify(free_rooms)
        used_rooms = []
        for start, end in meetings:
            while used_rooms and used_rooms[0][0] <= start:
                heappush(free_rooms, heappop(used_rooms)[1])
                
            if free_rooms:
                room = heappop(free_rooms)
                heappush(used_rooms, (end, room))
                counter[room] += 1
                continue
            
            time, room = heappop(used_rooms)
            heappush(used_rooms, (time + (end - start), room))
            counter[room] += 1
        
        lowest = 0
        result = -1
        for room, held in enumerate(counter):
            if held > lowest:
                result = room
                lowest = held
        return result
