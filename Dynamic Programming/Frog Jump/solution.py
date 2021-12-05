class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        positions = dict()
        for i, stone in enumerate(stones):
            positions[stone] = i
            
        @cache
        def jump(idx, prevIdx):
            if idx >= n - 1:
                return True
            lastJump = stones[idx] - stones[prevIdx]
            for i in range(-1, 2): # k - 1, k, k + 1
                nextJump = lastJump + i
				# Cannot jump backward
                if nextJump <= 0:
                    continue
                nextStone = stones[idx] + nextJump
                if nextStone in positions:
                    if(jump(positions[nextStone], idx)):
                        return True
            return False
        
        return jump(0, 0)
            