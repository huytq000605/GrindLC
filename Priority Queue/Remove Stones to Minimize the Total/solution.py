class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq = []
        for pile in piles:
            heappush(pq, -pile)
        while k:
            heappush(pq, -(-heappop(pq))//2)
            k -= 1
        return -sum(pq)
