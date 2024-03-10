class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        pq = []
        for num in nums[1:]:
            heappush(pq, -num)
            if len(pq) > 2:
                heappop(pq)
        return nums[0] - sum(pq)
