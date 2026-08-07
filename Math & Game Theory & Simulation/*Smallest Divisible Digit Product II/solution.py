class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        tc = t
        for f in (2,3,5,7):
            while tc % f == 0: tc //= f
        if tc != 1: return "-1"
        
        # try to form number has length = num
        n = len(num)
        m = n-1
        # ts[i] = t if keep num[:i]
        ts = [t for _ in range(n)]
        for i in range(n):
            if num[i] == '0':
                m = i
                break
            ts[i] = (ts[i-1] if i else t) // gcd(ts[i-1] if i else t, int(num[i]))
        if ts[-1] == 1: return num

        def fill(t, n):
            result = ""
            while t > 1:
                for i in range(9, -1, -1):
                    if t % i == 0:
                        result += str(i)
                        t //= i
                        n -= 1
                        break
            while n > 0:
                result += "1"
                n -= 1
            return result[::-1]
        # increase from idx m to idx 0
        for i in range(m, -1, -1):
            tc = ts[i-1] if i else t
            
            right_len = n - i - 1
            for d in range(int(num[i]) + 1, 10):
                right = fill(tc // gcd(tc, d), right_len)
                if len(right) == right_len:
                    return num[:i] + str(d) + right
            
        
        # if cannot find result with len == num
        return fill(t, n+1)

