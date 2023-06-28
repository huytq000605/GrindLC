class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        
        pq = [(-1, start)]
        rate = [0 for _ in range(n)]
        rate[start] = 1
        while pq:
            prob, u = heappop(pq)
            for v, p in graph[u]:
                if rate[v] < p * -prob:
                    rate[v] = p * -prob
                    heappush(pq, (-rate[v], v))

        return rate[end]  
