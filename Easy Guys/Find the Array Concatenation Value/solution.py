class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        nums = deque(nums)
        result = 0
        while nums:
            if len(nums) == 1:
                result += nums.pop()
            else:
                result += int(str(nums.popleft()) + str(nums.pop()))
        return result
            
