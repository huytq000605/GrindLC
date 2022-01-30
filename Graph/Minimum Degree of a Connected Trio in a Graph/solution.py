class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        graph = [[0 for j in range(n)] for i in range(n)]
        num_edges = [0 for i in range(n)]
        seen = set()
        for u, v in edges:
            graph[u - 1][v - 1] = 1
            graph[v - 1][u - 1] = 1
            num_edges[u-1] += 1
            num_edges[v-1] += 1
        result = math.inf
        for u in range(n):
            for v in range(u):
                if graph[u][v] == 0:
                    continue
                for z in range(v + 1, u):
                    if graph[u][z] == 0 or graph[v][z] == 0:
                        continue
                    result = min(result, num_edges[u] + num_edges[v] + num_edges[z] - 6)
        if result == math.inf:
            return -1
        return result
