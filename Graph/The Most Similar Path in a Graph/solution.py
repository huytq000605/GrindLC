class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:            
        graph = [[] for _ in range(n)]
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
            
        @cache
        def dfs(u, i):
            if i >= len(targetPath): return 0
            start = 0
            if names[u] == targetPath[i]:
                start = 1
            result = start
            for v in graph[u]:
                result = max(result, start + dfs(v, i + 1))
            return result
        
        expected = 0
        for u in range(n):
            expected = max(expected, dfs(u, 0))
        
        result = []
        met = 0
        i = 0
        while i < len(targetPath):
            if result: 
                adj = graph[result[-1]]
            else:
                adj = list(i for i in range(n))
            for v in adj:
                if dfs(v, i) == expected - met:
                    if names[v] == targetPath[i]:
                        met += 1
                    result.append(v)
                    i += 1
                    break
        return result
            
