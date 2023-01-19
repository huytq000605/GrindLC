class Solution:
    def confusingNumber(self, n: int) -> bool:
        num = n
        after = 0
        while n:
            d = n % 10
            if d in [2,3,4,5,7]: return False
            n //= 10
            if d == 6: d = 9
            elif d == 9: d = 6
            after = after * 10 + d
        return after != num
