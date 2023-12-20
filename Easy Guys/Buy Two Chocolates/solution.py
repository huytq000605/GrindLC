class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        pq = []
        for price in prices:
            heappush(pq, -price)
            if len(pq) > 2:
                heappop(pq)
        if -sum(pq) <= money:
            return money + sum(pq)
        else:
            return money
