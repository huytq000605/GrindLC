class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        pq = []
        neg = []
        for num in nums:
            heappush(pq, num)
            if len(pq) > 3: heappop(pq)
            if num < 0:
                heappush(neg, -num)
                if len(neg) > 2: heappop(neg)
        result = reduce(mul, pq)
        if len(neg) == 2: result = max(result, max(pq) * neg[0] * neg[1])
        return result
