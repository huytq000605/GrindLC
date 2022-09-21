class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        s = 0
        for num in nums:
            if num % 2 == 0:
                s += num
        for v, i in queries:
            if nums[i] % 2 == 0:
                s -= nums[i]
            nums[i] += v
            if nums[i] % 2 == 0:
                s += nums[i]
            result.append(s)
        return result
