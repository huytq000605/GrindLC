class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        @cache
        def dfs(i, k, prev, count):
            if i >= n:
                if count <= 1:
                    return len(prev)
                else:
                    return len(prev) + len(str(count))
            if s[i] == prev:
                result = dfs(i+1, k, prev, count + 1)
            else:
                plus = 0
                if count > 1:
                    plus = len(str(count))
                result = dfs(i+1, k, s[i], 1) + len(prev) + plus
            if k > 0:
                result = min(result, dfs(i+1, k-1, prev, count))
            return result
        return dfs(0, k, "", 0)
            
                
            
