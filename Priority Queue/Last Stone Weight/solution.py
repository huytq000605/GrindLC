class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        while len(maxHeap) > 0:
            maxStone = -heapq.heappop(maxHeap)
            if len(maxHeap) == 0:
                return maxStone
            secondStone = -heapq.heappop(maxHeap)
            remain = maxStone - secondStone
            if remain > 0:
                heapq.heappush(maxHeap, -remain)
        return 0