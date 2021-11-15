class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dfs(idx1, idx2):
            if idx1 >= len(s) and idx2 >= len(p): return True
            if idx2 >= len(p): return False
            if idx1 >= len(s):
                if (len(p) - idx2) % 2 == 1: return False
                for i in range(idx2 + 1, len(p), 2):
                    if p[i] != "*":
                        return False
                return True
            if idx2 < len(p) - 1 and p[idx2 + 1] == "*":
                if(dfs(idx1, idx2 + 2)): 
                    return True
                if p[idx2] == "." or s[idx1] == p[idx2]: 
                    return dfs(idx1 + 1, idx2)
                else: 
                    return False
            elif p[idx2] == "." or s[idx1] == p[idx2]:
                return dfs(idx1 + 1, idx2 + 1)
            else:
                return False
        
        return dfs(0, 0)