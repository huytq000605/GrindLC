class Solution:
    def countVowelPermutation(self, n: int) -> int:
        rules = {
            'a': 'e',
            'e': 'ai',
            'i': 'ueoa',
            'o': 'iu',
            'u': 'a',
            '': 'ueoai'
        }
        MOD = 1e9 + 7
        
        @lru_cache(None)
        def dfs(idx, prev):
            if idx >= n:
                return 1
            result = 0
            for l in rules[prev]:
                result += dfs(idx + 1, l)
                result = int(result % MOD)
            return result
            
        return dfs(0, '')