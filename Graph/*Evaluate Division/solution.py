class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (u, v), value in zip(equations, values):
            graph[u].append((v, value))
            graph[v].append((u, 1/value))
            
        result = [-1 for i in range(len(queries))]
        
        def dfs(u, target, seen):
            if u == target:
                return 1, True
            for v, value in graph[u]:
                if v in seen:
                    continue
                seen.add(v)
                ans, ok = dfs(v, target, seen)
                if ok:
                    return value * ans, True
            return 0, False
            
        
        for i, (u, v) in enumerate(queries):
            if u not in graph or v not in graph:
                continue
            ans, ok = dfs(u, v, set([u]))
            if ok:
                result[i] = ans
        return result