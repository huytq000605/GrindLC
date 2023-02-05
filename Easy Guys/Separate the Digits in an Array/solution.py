class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            for d in str(num):
                result.append(int(d))
        return result
