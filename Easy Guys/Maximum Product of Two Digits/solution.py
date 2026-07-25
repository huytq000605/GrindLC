class Solution:
    def maxProduct(self, n: int) -> int:
        pq = []
        while n:
            heappush(pq, n % 10)
            n //= 10
            if len(pq) > 2: heappop(pq)
        return pq[0] * pq[1]
