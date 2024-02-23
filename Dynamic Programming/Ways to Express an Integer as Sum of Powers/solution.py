MOD = 10**9 + 7
@cache
def dfs(n, num, x):
    if n == 0:
        return 1
    if num == 0:
        return 0
    while num**x > n:
        num -= 1
    result = 0
    while num > 0:
        result += dfs(n - num ** x, num - 1, x)
        result %= MOD
        num -= 1
    return result

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        num = 300
        while num**x > n:
            num -= 1
        return dfs(n, num, x)
