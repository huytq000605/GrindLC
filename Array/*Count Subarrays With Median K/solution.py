class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        idx = nums.index(k)
                
        balance = 0
        left = defaultdict(int)
        for i in reversed(range(idx+1)):
            if nums[i] > k:
                balance += 1
            elif nums[i] < k:
                balance -= 1
            left[balance] += 1
        balance = 0
        result = 0

        for i in range(idx, n):
            if nums[i] > k:
                balance += 1
            elif nums[i] < k:
                balance -= 1
            result += left[-balance] + left[-balance+1]
        return result
        
        



            
