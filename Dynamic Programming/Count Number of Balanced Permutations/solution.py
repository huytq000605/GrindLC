class Solution:
def countBalancedPermutations(self, num: str) -> int:
    MOD = 10**9 + 7
    counter = Counter([int(d) for d in num])
    @cache
    def dfs(d, odd, even, diff):
        if(d == 10): return diff == 0
        result = 0
        count = counter[d]
        if not count: return dfs(d+1, odd, even, diff)
        for o in range(min(count, odd) + 1):
            e = count - o
            if(e > even): continue
            result += dfs(d+1, odd - o, even - e, diff + o*d - e*d) * comb(odd, o) * comb(even, e)
            result %= MOD
        return result
    odd = len(num) // 2
    even = odd + len(num) % 2
    result = dfs(0, odd, even, 0)
    return result
    
        
        
