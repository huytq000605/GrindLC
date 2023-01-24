class Solution:
    def confusingNumberII(self, n: int) -> int:
        valids = [0,1,6,8,9]
        def rotate(num):
            result = 0
            while num:
                d = num % 10
                num //= 10
                if d == 9: d = 6
                elif d == 6: d = 9
                result = result * 10 + d
            return result
        
        result = 0
        def gen(cur):
            nonlocal result
            if cur > n:
                return
            if rotate(cur) != cur:
                result += 1
            for d in valids:
                gen(cur * 10 + d)
        for starting in valids[1:]:
            gen(starting)
        return result
                
            
