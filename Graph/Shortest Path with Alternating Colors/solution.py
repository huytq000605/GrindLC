class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in redEdges:
            graph[u].append((v, 0))
        for u, v in blueEdges:
            graph[u].append((v, 1))
        dq = deque([(0, 0, -1)])
        distance = [[-1 for _ in range(2)] for _ in range(n)]
        distance[0][0] = 0
        distance[0][1] = 0
        while dq:
            u, s, color = dq.popleft()
            for v, ncolor in graph[u]:
                if ncolor != color and distance[v][ncolor] == -1:
                    distance[v][ncolor] = s + 1
                    dq.append((v, s+1, ncolor))
        result = [-1 for _ in range(n)]
        for v in range(n):
            d = min(distance[v])
            if d == -1: result[v] = max(distance[v])
            else: result[v] = d
        return result
            
