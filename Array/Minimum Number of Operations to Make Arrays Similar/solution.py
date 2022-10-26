class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        nums.sort(key = lambda num: (num % 2, num))
        target.sort(key = lambda num: (num % 2, num))
        result = 0
        for i in range(n):
            ops = abs(target[i] - nums[i]) // 2
            result += ops
        return result // 2
        
