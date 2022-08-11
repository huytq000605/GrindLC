class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        restricted = set(restricted)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set([0])    
        
        def dfs(u):
            nonlocal seen, restricted
            result = 1
            for v in graph[u]:
                if v in seen or v in restricted:
                    continue
                seen.add(v)
                result += dfs(v)
            return result
        
        return dfs(0)
