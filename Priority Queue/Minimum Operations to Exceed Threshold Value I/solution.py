class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        result = 0
        while nums and nums[0] < k:
            heappop(nums)
            result += 1
        return result
