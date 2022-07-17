class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        seen = dict()
        result = -1
        for num in nums:
            sum_digit = 0
            current = num
            while current:
                sum_digit += current % 10
                current //= 10
            if sum_digit in seen:
                result = max(result, num + seen[sum_digit])
                seen[sum_digit] = max(seen[sum_digit], num)
            else:
                seen[sum_digit] = num
        return result
