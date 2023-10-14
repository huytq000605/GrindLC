class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(types)
        @cache
        def dfs(i, score):
            if i >= n:
                if score == target: return 1
                return 0
            result = 0
            count, mark = types[i]
            for c in range(count + 1):
                if score + mark * c > target: continue
                result += dfs(i + 1, score + mark * c)
                result %= MOD
            return result
        return dfs(0, 0)
            
