class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads) + 1
        graph = [[] for _ in range(n)]
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(u, p):
            total_people = 1
            total_steps = 0
            for v in graph[u]:
                if v == p: continue
                steps, people = dfs(v, u)
                total_steps += steps + math.ceil(people / seats)
                total_people += people
            return total_steps, total_people
        
        result, _ = dfs(0, -1)
        return result
