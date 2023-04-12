class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd = 0, 0
        flag = True
        while n:
            if flag:
                even += n % 2
            else:
                odd += n % 2
            flag = not flag
            n >>= 1
        return [even, odd]
