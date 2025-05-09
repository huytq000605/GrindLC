class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        counter = [0 for _ in range(10)]
        MOD = 10**9+7
        for d in num: counter[int(d)] += 1
        @cache
        def dfs(d, odd, even, diff):
            if d == 10: return diff == 0
            result = 0
            for e in range(0, min(even, counter[d]) + 1):
                o = counter[d] - e
                if o > odd: continue
                result += dfs(d+1, odd - o, even -  e, diff + (e-o) * d) * comb(even, e) * comb(odd, o)
                result %= MOD
            return result
        dfs.cache_clear()
        return dfs(0, len(num)//2, (len(num)+1)//2, 0)
