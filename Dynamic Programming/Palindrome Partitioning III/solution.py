class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        
        @cache
        def cost(i, j):
            if i >= j:
                return 0
            c = 0
            if s[i] != s[j]:
                c = 1
            return cost(i + 1, j - 1) + c
            
        @cache
        def dfs(i, k):
            if k < 0:
                return n
            if i >= n:
                if k == 0:
                    return 0
                return n
            result = n
            for j in range(i, n):
                result = min(result, cost(i, j) + dfs(j + 1, k - 1))
            return result
        
        return dfs(0, k)