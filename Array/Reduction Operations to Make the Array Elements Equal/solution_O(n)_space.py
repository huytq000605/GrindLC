class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        freq = dict()
        for num in nums:
            if num not in freq: freq[num] = 0
            freq[num] += 1
        values = sorted(freq.items(), reverse = True)
        numOfNumber = 0
        result = 0
        for i in range(len(values)):
            result += numOfNumber
            numOfNumber += values[i][1]
        return result