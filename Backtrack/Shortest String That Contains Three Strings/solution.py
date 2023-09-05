class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def fill(a, b):
            if b in a:
                return a
            l = len(b)
            for start in range(l-1, 0, -1):
                idx_a, idx_b = len(a)-1, start-1
                valid = True
                while idx_a >= 0 or idx_b >= 0:
                    if idx_a < 0 and idx_b < 0: 
                        break
                    elif idx_a < 0:
                        valid = False
                        break
                    elif idx_b < 0:
                        break
                    else:
                        if b[idx_b] != a[idx_a]:
                            valid = False
                            break
                        else:
                            idx_a -= 1
                            idx_b -= 1
                if valid:
                    a += b[start:]
                    return a
            return a + b
        
        def f(a, b, c):
            s = a
            s = fill(s, b)
            s = fill(s, c)
            return s

        results = sorted([f(a, b, c), f(a, c, b), f(b, a, c), f(b, c, a), f(c, a, b), f(c, b, a)], key = lambda e: (len(e), e))
        
        return results[0]
