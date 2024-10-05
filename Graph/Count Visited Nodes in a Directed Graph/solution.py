class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        result = [0 for _ in range(n)]
            
        def dfs(u, seen, i):
            nonlocal result
            seen[u] = i
            v = edges[u]
            # we know how many steps that is taking v to circle
            if result[v] != 0:
                for u, j in seen.items():
                    result[u] = i + 1 - j + result[v]
                return
            
            # found a circle
            if v in seen:
                circle_size = i - seen[v] + 1
                result[u] = circle_size
                first = seen[v]
                while v != u:
                    result[v] = circle_size
                    v = edges[v]
                    seen.pop(v)
                
                # for the ones that are not in circle
                for u, i in seen.items():
                    result[u] = circle_size + (first - i)    
                return
            
            dfs(v, seen, i + 1)

        for u in range(n):
            if result[u] == 0:
                dfs(u, dict(), 0)
        return result
