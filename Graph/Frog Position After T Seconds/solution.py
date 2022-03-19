class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = [[] for i in range(n)]
        for u, v in edges:
            u, v = u-1, v-1
            graph[u].append(v)
            graph[v].append(u)
        target -= 1
        result = 0
        seen = set([0])
        
        def dfs(u, chance, t):
            nonlocal result
            if t == 0:
                if u == target:
                    result += chance
                return
            
            next_node = []
            for v in graph[u]:
                if v in seen:
                    continue
                next_node.append(v)
            
            if len(next_node) == 0 and u == target:
                result += chance
            
            for v in next_node:
                seen.add(v)
                dfs(v, chance / len(next_node), t - 1)
                seen.remove(v)
            
        dfs(0, 1, t)
        return result