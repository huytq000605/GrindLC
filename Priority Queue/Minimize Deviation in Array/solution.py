class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        heap = []
        min_num = math.inf

        for num in nums:
            if num % 2 == 1:
                num *= 2
            heappush(heap, -num)
            min_num = min(min_num, num)
        
        result = math.inf
        
        while -heap[0] % 2 == 0:
            max_num = -heappop(heap)
            result = min(result, max_num - min_num)
            heappush(heap, -(max_num // 2))
            min_num = min(max_num // 2, min_num)
            
        result = min(result, -heap[0] - min_num)
        return result