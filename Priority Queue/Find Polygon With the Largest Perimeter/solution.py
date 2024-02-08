class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        result = sum(nums)
        pq = []
        for num in nums:
            heappush(pq, -num)
        while pq and result + pq[0] <= -pq[0]:
            result += heappop(pq)
        if len(pq) < 3:
            return -1
        return result
            
