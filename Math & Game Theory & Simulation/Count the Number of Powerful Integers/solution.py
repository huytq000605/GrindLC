class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        def lt(num):
            if int(s) > num:
                return 0
            snum = str(num)
            digit_to_fill = len(snum) - len(s)
            result = 0
            for digit in range(digit_to_fill):
                dnum = int(snum[digit])
                # at this point, we've already selected a smaller digit
                # so it's valid as long as the remaining digits are less than limit
                if limit < dnum:
                    return result + (limit+1) * (limit+1)**(digit_to_fill - digit - 1)
                result += dnum * (limit+1)**(digit_to_fill - digit - 1)
            # If we fill all the digits equal to num
            # need to check if the final number is <= num
            if int(snum[:digit_to_fill] + s) <= num:
                result += 1
            return result
        return lt(finish) - lt(start-1)
