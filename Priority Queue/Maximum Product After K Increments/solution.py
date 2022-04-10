class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heappush(pq, num)
        while k > 0:
            heappush(pq, heappop(pq) + 1)
            k -= 1
        result = pq.pop()
        while pq:
            result *= pq.pop()
            result %= 10**9 + 7
        return result