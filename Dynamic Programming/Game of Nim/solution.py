class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        mask = 0
        for i, pile in enumerate(piles):
            mask |= pile << (3*i)
        n = len(piles)
        
        @cache
        def dfs(mask):
            for i in range(n):
                piles = (mask >> (3 * i)) & 7
                for take in range(1, piles + 1):
                    new_mask = mask - (take << (3*i))
                    if not dfs(new_mask):
                        return True
            return False
        
        return dfs(mask)
            
