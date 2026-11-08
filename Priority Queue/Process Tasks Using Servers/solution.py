class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapify(free)
        busy = []
        time = 0
        result = [0 for _ in range(len(tasks))]
        for t, task in enumerate(tasks):
            time = max(time, t)
            while busy and busy[0][0] <= time:
                _, w, i = heappop(busy)
                heappush(free, (w, i))
            if free:
                w, i = heappop(free)
                heappush(busy, (time + task, w, i))
                result[t] = i
            else:
                time = busy[0][0]
                tt, w, i = heappop(busy)
                heappush(busy, (tt + task, w, i))
                result[t] = i
        return result
