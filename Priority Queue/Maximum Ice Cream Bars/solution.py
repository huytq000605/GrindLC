class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        pq = []
        for cost in costs:
            if coins < cost and pq and -pq[0] > cost:
                coins += -heappop(pq)
            if cost <= coins:
                coins -= cost
                heappush(pq, -cost)
        return len(pq)
                
