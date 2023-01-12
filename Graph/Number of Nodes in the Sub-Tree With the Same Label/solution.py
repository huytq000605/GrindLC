class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        result = [0 for i in range(n)]
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(u, p):
            nonlocal result
            res = [0 for i in range(26)]
            for v in graph[u]:
                if v == p: continue
                child = dfs(v, u)
                for i, v in enumerate(child):
                    res[i] += v
            idx = ord(labels[u]) - ord('a')
            res[idx] += 1
            result[u] = res[idx]    
            return res
        
        dfs(0, -1)
        return result
                
