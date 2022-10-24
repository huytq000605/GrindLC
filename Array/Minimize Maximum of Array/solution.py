class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result = nums[0]
        remaining = 0
        for i, num in enumerate(nums):
            if num <= result:
                remaining += result - num
            else:
                if remaining < (num - result):
                    num -= remaining
                    total = (result * i) + num
                    result = math.ceil(total / (i+1))
                    remaining = result * (i+1) - total
                else:
                    remaining -= (num - result)
        return result
