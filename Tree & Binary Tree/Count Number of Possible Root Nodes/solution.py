class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        graph = [[] for i in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        guesses = set(tuple(g) for g in guesses)
        
        @cache
        def dfs(u, p):
            correct_guess = 0
            for v in graph[u]:
                if v == p: continue
                if (u, v) in guesses:
                    correct_guess += 1
                correct_guess += dfs(v, u)
            return correct_guess
        
        result = 0
        for u in range(n):
            if dfs(u, -1) >= k:
                result += 1
        return result
