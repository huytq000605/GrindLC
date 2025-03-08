class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        black = 0
        result = k
        for i in range(len(blocks)):
            if i >= k:
                black -= (blocks[i-k] == 'B')
            black += blocks[i] == 'B'
            result = min(result, k - black)
        return result
