class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        result = [0 for _ in range(n)]
        
        def dfs(u, p, s):
            result = 0
            if s % signalSpeed == 0:
                result += 1
            for v, w in graph[u]:
                if v == p: continue
                result += dfs(v, u, s + w)
            return result
                
        for u in range(n):
            count = 0
            res = 0
            for v, w in graph[u]:
                dc = dfs(v, u, w)
                res += count * dc
                count += dc
            result[u] = res
        return result
                        
