class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0 for i in range(n + 1)]
        
        @cache
        def dfs(num):
            if num == 0:
                return 0
            return num % 2 + dfs(num // 2)
        
        for i in range(n, -1, -1):
            result[i] = dfs(i)
        
        return result