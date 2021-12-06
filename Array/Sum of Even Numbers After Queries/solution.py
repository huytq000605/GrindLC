class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even = 0
        for num in nums:
            if num % 2 == 0:
                even += num
        result = []
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                even -= nums[idx]
            nums[idx] += val
            if nums[idx] % 2 == 0:
                even += nums[idx]
            result.append(even)
        return result