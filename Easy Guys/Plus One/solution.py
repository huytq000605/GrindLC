class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = 1
        idx = len(digits) - 1
        while idx >= 0 and plus > 0:
            digits[idx] += 1
            plus = math.floor(digits[idx] / 10)
            digits[idx] = digits[idx] % 10
            idx -= 1
        if plus > 0:
            return [1, *digits]
        else:
            return digits