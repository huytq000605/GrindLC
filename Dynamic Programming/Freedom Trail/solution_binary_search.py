class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # dfs(i, j) = min(dfs(k, j+1) + cost for k in range(n))
        # dp[i] = dp[k] + cost for k i
        n = len(ring)
        dp = [0 for _ in range(n)]
        indexes = defaultdict(list)
        for i, v in enumerate(ring):
            indexes[v].append(i)

        for k in key[::-1]:
            ndp = [math.inf for _ in range(n)]
            for i in range(n):
                j = bisect.bisect_left(indexes[k], i)
                m = len(indexes[k])
                for d in range(-1, 1):
                    target = indexes[k][((j + d) + m) % m]
                    diff = abs(i - target)
                    cost = min(diff, n - diff) + 1
                    ndp[i] = min(ndp[i], dp[target] + cost)
            dp = ndp
        return min([dp[i] + min(i, n-i) for i in range(n)])
