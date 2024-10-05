class Solution:
    def stringCount(self, n: int) -> int:
        # nCk = n! / (n-k)! k!
        MOD = 10**9 + 7
        # first bit = l
        # second bit = t
        # third & fourth bit = e

        @cache
        def dfs(i, mask):
            if i >= n:
                if mask == (1 << 4) - 1:
                    return 1
                return 0
            if mask == (1 << 4) - 1:
                return pow(26, n-i, MOD)
            # Choose all characters except "lep"
            result = ((26 - 3) * dfs(i+1, mask)) % MOD
            result = (result + dfs(i+1, mask | 1)) % MOD # Choose "l"
            result = (result + dfs(i+1, mask | (1 << 1))) % MOD # Choose "t"
            # Choose "e"
            if (mask >> 2) & 1 == 1:
                result = (result + dfs(i+1, mask | (1 << 3))) % MOD
            else:
                result = (result + dfs(i+1, mask | (1 << 2))) % MOD
            return result
        
        return dfs(0, 0)
            
