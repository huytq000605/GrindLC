from sortedcontainers import SortedList

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        busy = []
        free = SortedList([i for i in range(k)])
        requests = [0 for i in range(k)]
        for i in range(len(arrival)):
            start, time = arrival[i], load[i]
            request = i % k
            while len(busy) > 0 and start >= busy[0][0]:
                free.add(heappop(busy)[1])
            if len(free) == 0:
                continue
            if request in free:
                free.discard(request)
                heappush(busy, (time + start, request))
                requests[request] += 1
            else:
                idx = (free.bisect_left(request)) % len(free)
                heappush(busy, (time + start, free[idx]))
                requests[free[idx]] += 1
                free.pop(idx)
        max_request = max(requests)
        result = []
        for i, r in enumerate(requests):
            if r == max_request:
                result.append(i)
        return result