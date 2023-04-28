class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        @cache
        def dfs(i, j):
            if j >= len(s2):
                return 0
            if i >= len(s1):
                return math.inf
            if s1[i] == s2[j]:
                return 1 + dfs(i+1,j+1)
            return 1 + dfs(i+1, j)
        result_len = math.inf
        result_idx = -1
        for i in range(len(s1)):
            l = dfs(i, 0)
            if l < result_len:
                result_len = l
                result_idx = i
        if result_idx == -1:
            return ""
        return s1[result_idx:result_idx + result_len]
            
