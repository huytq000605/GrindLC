class Solution:
    def myAtoi(self, s: str) -> int:
        white_space = True
        negative = 1
        result = 0
        for l in s:
            if l in "+-" and white_space:
                if l == "-":
                    negative = -1
                white_space = False
                continue
            elif l == " " and white_space:
                continue
            elif l != " ":
                white_space = False
        
            if l.isnumeric():
                result = result * 10 + int(l)
            else:
                break
                
        result = result * negative
        if result < -(1<<31):
            result = -(1<<31)
        elif result > (1<<31) - 1:
            result = (1<<31) - 1
        return result
