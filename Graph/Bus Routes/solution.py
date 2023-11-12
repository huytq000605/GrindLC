class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        buses = defaultdict(list)
        for i, route in enumerate(routes):
            for bus in route:
                buses[bus].append(i)
        
        dq = deque([(source, 0)])
        while dq:
            u, s = dq.popleft()
            if u == target:
                return s
            for route in buses[u]:
                for v in routes[route]:
                    dq.append((v, s + 1))
                routes[route] = []
            buses[u] = []
        return -1

