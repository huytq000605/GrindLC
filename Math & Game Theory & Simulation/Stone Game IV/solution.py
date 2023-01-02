class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def dfs(target):
            if target == 0:
                return False
            i = 1
            while i * i <= target:
                if not dfs(target - i * i):
                    return True
                i += 1
            return False
        
        return dfs(n)