class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        pq = [-num for num in nums]
        heapify(pq)
        result = 0
        while k:
            num = -heappop(pq)
            heappush(pq, -math.ceil(num / 3))
            result += num
            k -= 1
        return result
            
