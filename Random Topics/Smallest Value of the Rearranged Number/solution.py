class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        digits = Counter()
        find_max = False
        if num < 0:
            find_max = True
            num = -num
            
        min_digit = 9
        
        for d in str(num):
            digit = int(d)
            digits[digit] += 1
            if digit == 0:
                continue
            min_digit = min(min_digit, digit)
        
        result = ""
        if not find_max:
            result += str(min_digit)
            digits[min_digit] -= 1
            for i in range(10):
                while digits[i] > 0:
                    result += str(i)
                    digits[i] -= 1
            return int(result)
        else:
            for i in range(9, -1, -1):
                while digits[i] > 0:
                    result += str(i)
                    digits[i] -= 1
            return -int(result)