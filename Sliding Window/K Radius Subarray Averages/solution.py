class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = [-1] * n
        length = k*2 + 1
        start = 0
        total = 0
        
        for i in range(k * 2):
            if i >= n:
                return result
            total += nums[i]
        
        for end in range(k * 2, n):
            idx = end - k
            total += nums[end]
            result[idx] = int(total / length)
            total -= nums[start]
            start += 1
        return result
        