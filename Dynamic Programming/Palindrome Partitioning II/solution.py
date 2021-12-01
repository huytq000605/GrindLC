class Solution:
    def minCut(self, s: str) -> int:
        
        @lru_cache(None)
        def isPalindrome(left, right):
            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            return isPalindrome(left + 1, right - 1)
        
        @lru_cache(None)
        def dfs(idx):
            if idx >= len(s): return 0
            result = len(s) - idx
            for i in range(idx, len(s)):
                if isPalindrome(idx, i):
                    result = min(result, 1 + dfs(i + 1))
            return result
        
        return dfs(0) - 1