class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        m, n = len(nums), len(nums[0])
        for r in range(m):
            heapq.heapify(nums[r])
        result = 0
        for op in range(n):
            mx = 0
            for r in range(m):
                mx = max(heappop(nums[r]), mx)
            result += mx
        return result
        
