class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in connections:
            graph[u].append((v, 0))
            graph[v].append((u, 1))
        result = 0
        q = deque([0])
        while q:
            u = q.popleft()
            for v, d in graph[u]:
                if not graph[v]: continue
                if d == 0: result += 1 
                q.append(v)
            graph[u] = None
        return result
