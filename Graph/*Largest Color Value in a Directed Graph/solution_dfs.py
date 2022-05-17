class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        result = 0
        
        seen = [0 for i in range(n)]
        largest = [[0 for j in range(26)] for i in range(n)]
        graph = [[] for i in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            
        def dfs(node):
            if seen[node] == 1:
                return False
            if seen[node] == 2:
                return True
            seen[node] = 1
            for next_node in graph[node]:
                if not dfs(next_node):
                    return False
                for i in range(26):
                    largest[node][i] = max(largest[node][i], largest[next_node][i])
            largest[node][ord(colors[node]) - ord('a')] += 1
            seen[node] = 2
            return True
        
        for node in range(n):
            if not dfs(node):
                return -1
            result = max(result, max(largest[node]))
            
        return result