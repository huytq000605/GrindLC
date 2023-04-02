class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        result = math.inf
        for u in range(n):
            parent = [-1 for _ in range(n)]
            ds = [math.inf for _ in range(n)]
            ds[u] = 0
            dq = deque([u])
            while dq:
                u = dq.popleft()
                for v in graph[u]:
                    if ds[v] == math.inf:
                        ds[v] = ds[u] + 1
                        parent[v] = u
                        dq.append(v)
                    elif v != parent[u]:
                        result = min(result, ds[u] + ds[v] + 1)
        if result == math.inf: return -1
        return result
