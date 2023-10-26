class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        result = 0
        def dfs(u, p):
            nonlocal result
            s = values[u]
            for v in tree[u]:
                if v == p: continue
                value = dfs(v, u)
                s += value
            if s % k == 0:
                result += 1
            return s % k
        
        dfs(0, -1)
        return result
            
