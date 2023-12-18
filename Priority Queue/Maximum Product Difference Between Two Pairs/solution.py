class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min_heap, max_heap = [], []
        for num in nums:
            heappush(max_heap, -num)
            heappush(min_heap, num)
            if len(max_heap) > 2:
                heappop(max_heap)
            if len(min_heap) > 2:
                heappop(min_heap)
        w, x = max_heap
        y, z = min_heap
        return (y*z) - (w*x)
