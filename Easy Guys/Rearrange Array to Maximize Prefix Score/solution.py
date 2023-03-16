class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        neg = sorted([nums[i] for i in range(n) if nums[i] < 0], reverse = True)
        pos = [nums[i] for i in range(n) if nums[i] > 0]
        zeros = [nums[i] for i in range(n) if nums[i] == 0]
        
        result = len(pos)
        if result == 0:
            return 0
        result += len(zeros)
        s = sum(pos)
        
        for num in neg:
            if s + num > 0:
                result += 1
                s += num
        return result
                
