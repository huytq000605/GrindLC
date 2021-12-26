class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split("=")
        
        def cal(s):
            X, Num = 0, 0
            sign, currentNum = "+", 0
            x, zero = False, False
            for l in s:
                if l == "+" or l == "-":
                    if sign == "-":
                        currentNum = -currentNum
                    if x:
                        if currentNum == 0 and zero == False:
                            if sign == "+":
                                currentNum = 1
                            else:
                                currentNum = -1
                        X += currentNum
                    else:
                        Num += currentNum
                    sign = l
                    currentNum = 0
                    zero = False
                    x = False
                elif l.isnumeric():
                    if l == "0":
                        zero = True
                    currentNum = currentNum * 10 + int(l)
                elif l == "x":
                    x = True

            if sign == "-":
                currentNum = -currentNum
            if x:
                if currentNum == 0 and zero == False:
                    if sign == "+":
                        currentNum = 1
                    else:
                        currentNum = -1
                X += currentNum
            else:
                Num += currentNum
            
            return X, Num
        
        left_x, left_num = cal(left)
        right_x, right_num = cal(right)
        
        if left_x - right_x == 0 and right_num - left_num == 0:
            return "Infinite solutions"
        if left_x - right_x == 0:
            return "No solution"
        return f"x={(right_num - left_num) // (left_x - right_x)}"