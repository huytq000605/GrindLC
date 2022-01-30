class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negative = []
        positive = []
        for num in nums:
            if num < 0:
                negative.append(num)
            else:
                positive.append(num)
        result = []
        for i in range(len(negative)):
            result.append(positive[i])
            result.append(negative[i])
        return result