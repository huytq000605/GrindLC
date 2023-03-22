class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v, d in roads:
            u, v = u-1, v-1
            graph[u].append((v, d))
            graph[v].append((u, d))
        q = [0]
        seen = [0 for _ in range(n)]
        result = math.inf
        while q:
            u = q.pop()
            for v, d in graph[u]:
                result = min(result, d)
                if seen[v]: continue
                seen[v] = 1
                q.append(v)
        return result
