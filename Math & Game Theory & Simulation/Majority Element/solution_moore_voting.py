class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        result = 0
        for num in nums:
            if count == 0:
                result = num
                count += 1
            elif num == result:
                count += 1
            else:
                count -= 1
        return result
