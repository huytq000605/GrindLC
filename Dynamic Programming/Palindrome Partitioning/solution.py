class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        @cache
        def is_palindrome(start, end):
            if start >= end:
                return True
            if s[start] != s[end]:
                return False
            return is_palindrome(start + 1, end - 1)
        
        result = []
        current = []
        def dfs(idx):
            nonlocal result, current
            if idx >= n:
                result.append([*current])
                return
            for i in range(idx, n):
                if is_palindrome(idx, i):
                    current.append(s[idx:i+1])
                    dfs(i + 1)
                    current.pop()
        dfs(0)
        return result
