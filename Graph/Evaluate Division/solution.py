class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for i, eq in enumerate(equations):
            a, b = eq
            v = values[i]
            graph[b][a] = v
            graph[a][b] = 1/v

        def dfs(a, b, seen):
            if a == b: return 1
            for c, v in graph[b].items():
                if c in seen: continue
                seen.add(c)
                a_div_c = dfs(a, c, seen)
                if a_div_c != -1: return a_div_c * v
            return -1
        
        result = [-1 for _ in range(len(queries))]
        for i, (a, b) in enumerate(queries):
            if a not in graph or b not in graph: continue
            result[i] = dfs(a, b, set([b]))
        return result
