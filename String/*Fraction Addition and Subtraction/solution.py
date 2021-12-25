class Solution:
    def fractionAddition(self, expression: str) -> str:
        sign = "+"
        top, bottom = 0, 0
        fill_bottom = False
        
        cur_top, cur_bottom = 0, 1
        
        for i, l in enumerate(expression):
            if l == "/":
                fill_bottom = True
            elif l == "+" or l == "-":
                if i == 0:
                    sign = l
                    continue
                same_bottom = math.lcm(bottom, cur_bottom)
                top = top * (same_bottom // bottom)
                cur_top = cur_top * (same_bottom // cur_bottom)
                bottom, cur_bottom = same_bottom, same_bottom
                if sign == "-":
                    top = -top
                cur_top += top
                top, bottom = 0, 0
                sign = l
                fill_bottom = False
            else:
                if not fill_bottom:
                    top = top * 10 + int(l)
                else:
                    bottom = bottom * 10 + int(l)
        
        same_bottom = math.lcm(bottom, cur_bottom)
        top = top * (same_bottom // bottom)
        cur_top = cur_top * (same_bottom // cur_bottom)
        bottom, cur_bottom = same_bottom, same_bottom
        if sign == "-":
            top = -top
        cur_top += top
        
        find_gcd = math.gcd(cur_top, cur_bottom)
        return f"{cur_top//find_gcd}/{cur_bottom//find_gcd}"