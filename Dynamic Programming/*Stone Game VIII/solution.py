class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefix = [0 for i in range(len(stones))]
        for idx, stone in enumerate(stones):
            if idx > 0:
                prefix[idx] = prefix[idx - 1]
            prefix[idx] += stone
        
        prefix = prefix[1:]
        
        @cache
        def dfs(idx):
            if idx == len(stones) - 1:
                return prefix[-1]
            # Keep going or get the idx as point and give turn
            return max(dfs(idx + 1), prefix[idx - 1] - dfs(idx + 1))
        return dfs(1)