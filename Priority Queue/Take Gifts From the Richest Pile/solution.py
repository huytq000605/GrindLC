class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        pq = []
        for gift in gifts:
            heappush(pq, -gift)
        for _ in range(k):
            
            heappush(pq, -math.floor(math.sqrt(-heappop(pq))))
        return -sum(pq)
