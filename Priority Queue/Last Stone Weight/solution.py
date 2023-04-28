class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-stone for stone in stones]
        heapify(pq)
        while len(pq) > 1:
            u, v = -heappop(pq), -heappop(pq)
            if u - v: heappush(pq, (v - u))
        if pq: return -pq[0]
        return 0
