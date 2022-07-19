class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # n = (x+1) + (x+2) + (x+3) + ... (x+k)
        # n = kx + k*(k+1)/2
        k = 2
        # n itself is a result in this question
        result = 1
        while n - k*(k+1)//2 >= 0:
            remaining = n - k*(k+1)//2
            if remaining % k == 0:
                result += 1
            k += 1
        return result
