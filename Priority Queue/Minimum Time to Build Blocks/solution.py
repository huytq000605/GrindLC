class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        # think about the last state
        # we need n workers = len(blocks)
        # and we should handle biggest block first
        
        heapify(blocks)
        while len(blocks) > 1:
            u, v = heappop(blocks), heappop(blocks)
            heappush(blocks, max(u, v) + split)
        return blocks[0]
            
            
