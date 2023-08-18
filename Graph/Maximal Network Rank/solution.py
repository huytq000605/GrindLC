class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        s = set()
        degree = [0 for _ in range(n)]
        for u, v in roads:
            degree[u] += 1
            degree[v] += 1
            if u > v:
                u, v = v, u
            s.add((u, v))
        result = 0
        for u in range(n):
            for v in range(u+1, n):
                res = degree[u] + degree[v]
                if (u, v) in s:
                    res -= 1
                result = max(result, res)
        return result
