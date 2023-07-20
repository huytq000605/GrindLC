class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        counter = Counter()
        dominant = 0
        for num in nums:
            counter[num] += 1
            if counter[num] * 2 > n:
                dominant = num
        
        left = 0
        right = counter[dominant]
        for i in range(n):
            if nums[i] == dominant:
                left += 1
                right -= 1
            if left * 2 > (i+1) and right * 2 > (n-1-i):
                return i
        return -1
            
        
        
