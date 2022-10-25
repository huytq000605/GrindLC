class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counter = [0 for i in range(n)]
        for num in nums:
            counter[num-1] += 1
        result = [0, 0]
        for k, v in enumerate(counter):
            if v == 0:
                result[1] = k+1
            if v > 1:
                result[0] = k+1
        return result
