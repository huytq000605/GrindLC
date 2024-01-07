class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) % 2 == 0:
            median = (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) // 2
        else:
            median = nums[len(nums) // 2]

        def is_palindrome(num):
            return str(num) == str(num)[::-1]
        
        # can optimize this with finding nearest smaller/ bigger palindrome
        nxt, prev = median, median
        while not is_palindrome(nxt):
            nxt += 1
        while not is_palindrome(prev):
            prev -= 1
        
        def cal(target):
            return sum(abs(num - target) for num in nums)
        return min(cal(prev), cal(nxt))
        
