class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = [[] for _ in range(n)]
        self.n = n
        for u, v, c in edges:
            self.graph[u].append((v, c))

    def addEdge(self, edge: List[int]) -> None:
        u, v, c = edge
        self.graph[u].append((v, c))

    def shortestPath(self, node1: int, node2: int) -> int:
        pq = [(0, node1)]
        ds = [math.inf for _ in range(self.n)]
        ds[node1] = 0
        while pq:
            s, u = heappop(pq)
            if u == node2:
                return s
            for v, c in self.graph[u]:
                if s + c < ds[v]:
                    ds[v] = s + c
                    heappush(pq, (s+c, v))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
