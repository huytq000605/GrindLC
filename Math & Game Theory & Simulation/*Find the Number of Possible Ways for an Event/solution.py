MOD = 10**9 + 7
@cache
def p(m, n):
    if n == 0 and m == 0: return 1
    if n == 0: return 0
    res = (m * p(m, n-1)) % MOD
    if m: res += (m * p(m-1, n-1)) % MOD
    return res % MOD

class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        result = 0
        # x could be fixed from 1 to n
        for m in range(1, min(n, x) + 1):
            # choosing m stages from x stages
            res = math.comb(x, m) % MOD
            # putting n people into m stages
            res = (res * p(m, n)) % MOD
            # award for each stage
            res = (res * pow(y, m, MOD)) % MOD
            result = (result + res) % MOD
        return result
            
