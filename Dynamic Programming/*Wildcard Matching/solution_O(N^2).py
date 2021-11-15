class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dfs(idx1, idx2):
            if idx1 >= len(s) and idx2 >= len(p):
                return True
            if idx1 >= len(s):
                for i in range(idx2, len(p)):
                    if p[i] != "*": return False
                return True
            if idx2 >= len(p):
                return False
            if s[idx1] == p[idx2]:
                return dfs(idx1 + 1, idx2 + 1)
            elif p[idx2] == "?":
                return dfs(idx1 + 1, idx2 + 1)
            elif p[idx2] == "*": # Tricky
                if dfs(idx1, idx2 + 1): # Match nothing
                    return True
                return dfs(idx1 + 1, idx2) # Match one or more
            else:
                return False
            
        return dfs(0, 0)