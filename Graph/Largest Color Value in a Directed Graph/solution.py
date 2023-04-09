class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
        colors = [ord(colors[u]) - ord('a') for u in range(n)]
        dp = [[0 for j in range(26)] for i in range(n)]
        circle = [0 for _ in range(n)]
        def dfs(u):
            if circle[u] == 1: return False
            if circle[u] == 2: return True
            circle[u] = 1
            for v in graph[u]:
                if not dfs(v): return False
                for color in range(26):
                    dp[u][color] = max(dp[u][color], dp[v][color])
            dp[u][colors[u]] += 1
            circle[u] = 2
            return True
        
        result = 0
        for u in range(n):
            if not dfs(u): return -1
            result = max(result, max(dp[u]))
        return result
                
