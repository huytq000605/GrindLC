class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        powers = sorted(Counter(power).items(), key = lambda p: p[0])
        @cache
        def dfs(i):
            if i >= len(powers): return 0
            return max(dfs(i+1), 
                       powers[i][1] * powers[i][0] + dfs(bisect.bisect_left(powers, powers[i][0] + 3, key = lambda p: p[0]))
                      )
        return dfs(0)
