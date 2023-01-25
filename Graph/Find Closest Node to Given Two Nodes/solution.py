class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        d1 = [-1 for _ in range(n)]
        d2 = [-1 for _ in range(n)]
        
        def dfs(u, d):
            s = 0
            d[u] = 0
            v = edges[u]
            while v != -1 and d[v] == -1:
                s += 1
                d[v] = s
                v = edges[v]
        
        dfs(node1, d1)
        dfs(node2, d2)
        
        d = math.inf
        result = -1
        for u in range(n):
            if d1[u] != -1 and d2[u] != -1:
                mx = max(d1[u], d2[u])
                if mx < d:
                    d = mx
                    result = u
        return result
