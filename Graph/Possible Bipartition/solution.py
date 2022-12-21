class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for i in range(n)]
        colors = [0 for i in range(n)]
        for u, v in dislikes:
            u, v = u-1, v-1
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(u, color):
            if colors[u] != 0:
                if colors[u] != color:
                    return False
                return True
            colors[u] = color
            for v in graph[u]:
                if not dfs(v, 3 - color):
                    return False
            return True
        
        for u in range(n):
            if colors[u] == 0:
                if not dfs(u, 1):
                    return False
        return True
