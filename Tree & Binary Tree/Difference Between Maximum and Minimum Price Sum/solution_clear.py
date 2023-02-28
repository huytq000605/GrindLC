class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        paths = [[(0, i)] for i in range(n)]
        graph = [[] for i in range(n)]
        parent = [-1 for i in range(n)]
        order = []
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        def dfs(u, p):
            nonlocal order, parent
            parent[u] = p
            order.append(u)
            for v in graph[u]:
                if v == p: continue
                heappush(paths[u], (dfs(v, u) + price[v], v))
                if len(paths[u]) > 2:
                    heappop(paths[u])
            longest_path = 0
            for path, vertice in paths[u]:
                longest_path = max(longest_path, path)
            return longest_path
        
        dfs(0, -1)
        for u in order:
            if parent[u] == -1:
                continue
            p = parent[u]
            
            longest_path = price[p]
            for path, vertice in paths[p]:
                if vertice != u:
                    longest_path = max(longest_path, path + price[p])
            heappush(paths[u], (longest_path, p))
            if len(paths[u]) > 2:
                heappop(paths[u])
        
        result = 0
        for u in range(n):
            result = max(result, max(map(lambda i: i[0], paths[u])))
        return result
                
