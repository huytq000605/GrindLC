class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        seen = set()
        result = -1
        # Try to find cycle in each traversal
        # If we've traversed to a node before, we won't find anything if do it again
        for u in range(n):
            if u in seen:
                continue
            seen.add(u)
            cycle = dict()
            cycle[u] = 0
            cur = 0
            while True:
                v = edges[u]
                cur += 1
                if v in cycle:
                    result = max(result, cur - cycle[v])
                if v == -1 or v in seen:
                    break
                seen.add(v)
                cycle[v] = cur
                u = v
        return result
