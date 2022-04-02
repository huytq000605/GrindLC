class Solution:
    def brokenCalc(self, value: int, target: int) -> int:
        result = 0
        while value < target:
            if target % 2 == 1:
                target += 1
                result += 1
            else:
                target //= 2
                result += 1
        return result + value - target