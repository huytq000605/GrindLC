class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        graph = [[] for i in range(n)]
        reversed_graph = [[] for i in range(n)]
        edges.sort(key = lambda edge: edge[2])
        
        for u, v, w in edges:
            graph[u].append((v, w))
            reversed_graph[v].append((u, w))
        
        distance_src1 = [math.inf for i in range(n)]
        distance_src2 = [math.inf for i in range(n)]
        distance_dest = [math.inf for i in range(n)]
        
        
        def dijkstra(source, distance, graph):
            distance[source] = 0
            pq = [(0, source)]
            while pq:
                current_w, u = heappop(pq)
                for v, w in graph[u]:
                    if current_w + w < distance[v]:
                        distance[v] = current_w + w
                        heappush(pq, (distance[v], v))
        
        dijkstra(src1, distance_src1, graph)
        dijkstra(src2, distance_src2, graph)
        dijkstra(dest, distance_dest, reversed_graph)
        
        result = math.inf
        for i in range(n):
            if distance_src1[i] == math.inf or distance_src2[i] == math.inf or distance_dest[i] == math.inf:
                continue
            result = min(result, distance_src1[i] + distance_src2[i] + distance_dest[i])
        if result == math.inf:
            return -1
        return result