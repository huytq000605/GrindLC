class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        min_idx = [n for i in range(n)]
        for center in range(n):
            start, end = center, center
            while start >= 0 and end < n:
                if s[start] != s[end]:
                    break
                if end - start + 1 >= k:
                    min_idx[start] = min(min_idx[start], end)
                start -= 1
                end += 1
            
            start, end = center, center + 1
            while start >= 0 and end < n:
                if s[start] != s[end]:
                    break
                if end - start + 1 >= k:
                    min_idx[start] = min(min_idx[start], end)
                start -= 1
                end += 1
        
        @cache
        def dfs(start):
            result = 0
            if start >= n:
                return 0
            if min_idx[start] != n:
                result = max(result, dfs(min_idx[start] + 1) + 1)
            result = max(result, dfs(start + 1))
            return result
        
        return dfs(0)
                
