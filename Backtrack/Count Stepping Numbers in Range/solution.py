class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        n1, n2 = len(low), len(high)
        result = 0
        MOD = 10**9 + 7
        
        @cache
        def dfs(i, goal, prev, lower, higher):
            if i >= goal:
                return 1
            result = 0

            if i == 0:
                start = 1
                end = 9
            else:
                start = max(0, prev - 1)
                end = min(9, prev + 1)
            for choose in range(start, end + 1):
                if choose == prev: continue
                if lower != -1 and choose < int(lower[i]): continue
                if higher != -1 and choose > int(higher[i]): continue
                next_lower, next_higher = -1, -1
                if lower != -1 and choose == int(lower[i]): next_lower = lower
                if higher != -1 and choose == int(higher[i]): next_higher = higher
                result += dfs(i+1, goal, choose, next_lower, next_higher)
                result %= MOD
            return result
                
        
        for n in range(n1+1, n2):
            result += dfs(0, n, -1, -1, -1)
            result %= MOD
        
        if n1 == n2:
            result += dfs(0, n1, -1, low, high)
            result %= MOD
            
        else:
            result += dfs(0, n1, -1, low, -1)
            result %= MOD
            result += dfs(0, n2, -1, -1, high)
            result %= MOD
        return result
