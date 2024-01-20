class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = [[] for _ in range(26)]
        offset = ord('a')
        for u, v, c in zip(original, changed, cost):
            u, v = ord(u) - offset, ord(v) - offset 
            graph[u].append((v, c))
        
        distances = [[math.inf for _ in range(26)] for _ in range(26)]
        for start in range(26):
            distances[start][start] = 0
            pq = [(0, start)]
            while pq:
                d, u = heappop(pq)
                for v, c in graph[u]:
                    if d + c < distances[start][v]:
                        distances[start][v] = d + c
                        heappush(pq, (d + c, v))
        result = 0
        for u, v in zip(source, target):
            u, v = ord(u) - offset, ord(v) - offset 
            if u != v:
                result += distances[u][v]
        if result == math.inf:
            return -1
        return result
            
