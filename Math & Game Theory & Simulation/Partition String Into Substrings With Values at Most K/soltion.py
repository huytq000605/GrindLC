class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        n = len(s)
        @cache
        def dfs(i):
            if i >= n:
                return 0
            num = ""
            result = math.inf
            for j in range(9):
                if i + j >= n:
                    break
                num += s[i+j]
                if int(num) > k:
                    break
                result = min(result, 1 + dfs(i + j + 1))
            return result
        result = dfs(0)
        if result == math.inf:
            return -1
        return result
                
                
                
