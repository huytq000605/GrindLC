class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = [[]]
        for num in nums:
            if len(result[-1]) == 3:
                result.append([])
            if result[-1] and num - result[-1][0] > k:
                return []
            result[-1].append(num)
        return result
