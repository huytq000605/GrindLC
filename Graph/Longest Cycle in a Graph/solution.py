class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        seen = [0 for _ in range(n)]
        result = -1
    
        for u in range(n):
            if seen[u]: continue
            cycle = dict()
            cur = 0
            cycle[u] = 0
            while True:
                v = edges[u]
                if v in cycle:
                    result = max(result, cur - cycle[v] + 1)
                if v == -1 or seen[v]: break
                seen[v] = 1
                cur += 1
                cycle[v] = cur
                u = v
        return result
            
