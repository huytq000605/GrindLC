class Solution:
    def canCross(self, stones: List[int]) -> bool:
        pos = dict()
        for i, stone in enumerate(stones):
            pos[stone] = i

        if stones[1] - stones[0] != 1:
            return False

        @cache
        def dfs(i, prev):
            if i == len(stones) - 1:
                return True
            last_jump = stones[i] - stones[prev]
            for next_jump in range(last_jump-1, last_jump+2):
                if next_jump <= 0: continue
                if stones[i] + next_jump in pos:
                    next_stone = stones[i] + next_jump
                    if dfs(pos[next_stone], i):
                        return True
            return False
        
        return dfs(1, 0)
