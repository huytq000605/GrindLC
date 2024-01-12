class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        pq = []
        m = len(values)
        n = len(values[0])
        for shop in range(m):
            heappush(pq, (values[shop][n-1], shop, n-1))
        result = 0
        day = 0
        while pq:
            day += 1
            cost, shop, pos = heappop(pq)
            result += day * cost
            if pos > 0:
                heappush(pq, (values[shop][pos - 1], shop, pos - 1))
        return result
            
