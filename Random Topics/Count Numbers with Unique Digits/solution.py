class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        def count(noOfDigits):
            if noOfDigits == 1:
                return 10
            result = 0
            num = 9
            for i in range(noOfDigits):
                if i == 0:
                    result = 9
                else:
                    result *= num
                    num -= 1
            return result
        result = 0
        for i in range(1, n + 1):
            result += count(i)
        return result