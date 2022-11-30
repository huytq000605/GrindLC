class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        n = len(s)
        MOD = 10**9 + 7
        @cache
        def dfs(i, parts, in_str):
            if i >= n:
                if not in_str and parts == k:
                    return 1
                return 0
            
            if not in_str:
                if s[i] not in ["2", "3", "5", "7"]:
                    return 0
                return dfs(i+minLength-1, parts+1, True) % MOD
            else:
                result = 0
                if s[i] not in ["2", "3", "5", "7"]:
                    result += dfs(i+1, parts, False)
                result += dfs(i+1, parts, True)
                result %= MOD
                
            return result
        return dfs(0, 0, False)
