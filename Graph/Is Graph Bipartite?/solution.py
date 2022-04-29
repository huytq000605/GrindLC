class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        set_of = [-1 for i in range(n)]
        
        def dfs(node, s):
            if set_of[node] == s:
                return True
            elif set_of[node] == -1:
                set_of[node] = s
            else:
                return False
            for next_node in graph[node]:
                if not dfs(next_node, 1-s):
                    return False
            return True
        
        for i in range(n):
            if set_of[i] == -1:
                if not dfs(i, 0):
                    return False
        return True