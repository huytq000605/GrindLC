class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        if num == 0:
            return True
        for i in range(num):
            j = int(str(i)[::-1])
            if i + j == num:
                return True
        return False
