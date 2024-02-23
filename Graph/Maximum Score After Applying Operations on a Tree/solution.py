class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(edges)
        tree = [[] for _ in range(n+1)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
            
        @cache
        def dfs(u, p):
            if len(tree[u]) == 1 and tree[u][0] == p:
                return values[u]
            result = min(values[u], sum(dfs(v, u) for v in tree[u] if v != p))
            return result
        return sum(values) - dfs(0, -1)
