class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        graph = [[] for i in range(n)]
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(u, prev):
            total_people, total_fuel = 1, 0
            for v in graph[u]:
                if v == prev:
                    continue
                people, fuel = dfs(v, u)
                total_people += people
                total_fuel += fuel
            cars = int(math.ceil(total_people / seats)) if u != 0 else 0
            return (total_people, total_fuel + cars)
        
        return dfs(0, -1)[1]
