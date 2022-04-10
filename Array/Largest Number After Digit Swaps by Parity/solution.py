class Solution:
    def largestInteger(self, num: int) -> int:
        digits = [0 for i in range(10)]
        num = str(num)
        even, odd = [], []
        for d in num:
            d = int(d)
            if d % 2 == 0:
                even.append(d)
            else:
                odd.append(d)
        odd = sorted(odd)
        even = sorted(even)
        result = 0
        for i in range(len(num)):
            if int(num[i]) % 2 == 0:
                result = result * 10 + even.pop()
            else:
                result = result * 10 + odd.pop()
        return result