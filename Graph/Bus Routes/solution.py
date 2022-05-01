class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        for bus, bus_stops in enumerate(routes):
            for bus_stop in bus_stops:
                graph[bus_stop].append(bus)
        q = deque([(source, 0)])
        while q:
            bus, step = q.popleft()
            if bus == target:
                return step
            for bus_stop in graph[bus]:
                for next_bus in routes[bus_stop]:
                    q.append((next_bus, step + 1))
                routes[bus_stop] = []
            graph[bus] = []
        return -1