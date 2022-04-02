class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = 0
        pq = []
        for num in nums:
            heappush(pq, -num)
            total += num
        reduced = 0
        step = 0
        while reduced < total / 2:
            num = -heappop(pq)
            reduced += num / 2
            num = num / 2
            heappush(pq, -num)
            step += 1
        return step