class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(parent)
        graph = [[] for i in range(n)]
        for u in range(1, n):
            graph[parent[u]].append(u)
            graph[u].append(parent[u])
        
        result = 1
        def dfs(u, p):
            nonlocal result
            longest_path = 1
            pq = []
            for v in graph[u]:
                if v == p: continue
                path = dfs(v, u)
                if s[u] != s[v]:
                    longest_path = max(longest_path, 1 + path)
                    heappush(pq, path)
                    if len(pq) > 2:
                        heappop(pq)
                result = max(result, sum(pq) + 1)
            return longest_path
        dfs(0, -1)
        return result
