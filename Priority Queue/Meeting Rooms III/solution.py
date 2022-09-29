class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free = [i for i in range(n)]
        meetings.sort()
        busy = []
        freq = [0 for i in range(n)]

        for start, end in meetings:
            while busy and start >= busy[0][0]:
                _, room = heappop(busy)
                heappush(free, room)

            if free:
                room = heappop(free)
                heappush(busy, (end, room))
            else:
                duration = end - start
                free_time, room = heappop(busy)
                heappush(busy, (free_time + duration, room))
            freq[room] += 1

        max_times = 0
        result = 0
        for room, times in enumerate(freq):
            if times > max_times:
                result = room
                max_times = times
        return result
