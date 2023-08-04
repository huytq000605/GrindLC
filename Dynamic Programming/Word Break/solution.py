class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        @cache
        def dfs(i):
            if i >= n:
                return True
            for j in range(i, n):
                if s[i:j+1] in words and dfs(j+1):
                    return True
            return False
        return dfs(0)
