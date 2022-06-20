class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        if k == 0:
            if num % 10 == 0:
                return 1
            return -1
        i = 1
        while k*i <= num:
            if (num - k*i) % 10 == 0:
                return i
            i += 1
        return -1
            