class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # a numbers
        # base*a + (a + 1) * a // 2
        i = 2
        result = 0
        while True:
            plus = (i+1) * i // 2
            base = n-plus
            if base < 0:
                break
            if base % i == 0:
                result += 1
            i += 1
            
        return result + 1