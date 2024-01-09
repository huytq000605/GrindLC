class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(edges) + 1
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        # (u, v) <= 10**5
        # half < 14
        @cache
        def dfs(u, p, half):
            if half >= 14:
                return 0
            return max( (coins[u] >> half) - k + sum(dfs(v, u, half) for v in tree[u] if v != p), \
                        (coins[u] >> half) // 2 + sum(dfs(v, u, half + 1) for v in tree[u] if v != p) )
        return dfs(0, -1, 0)
