class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        seen = set()
        for start, end in connections:
            graph[start].append((end, 1))
            graph[end].append((start, 0))
        
        result = 0
        seen.add(0)
        def dfs(node):
            nonlocal result
            for next_node, take in graph[node]:
                if next_node in seen:
                    continue
                seen.add(next_node)
                result += take
                dfs(next_node)
        dfs(0)  
        return result