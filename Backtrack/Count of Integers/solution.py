class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7
        d1, d2 = len(num1), len(num2)

        # count how many number have n digist which sum digit is in range
        @cache
        def dfs(ith: int, s: int, n: int) -> int:
            if ith >= n:
                if s >= min_sum and s <= max_sum:
                    return 1
                return 0
            result = 0
            for i in range(10):
                result += dfs(ith+1, min(s+i, max_sum+1), n)
                result %= MOD
            return result
        
        # count how many number < num, which have sum digit in range 
        def count(num: str) -> int:
            n = len(num)
            result = 0
            s = 0
            for length in range(1, n):
                for first_digit in range(1, 10):
                    result = (result + dfs(1, first_digit, length)) % MOD
            for nth in range(n):
                d_num = int(num[nth])
                if nth == 0:
                    for d in range(1, d_num):
                        result = (result + dfs(nth + 1, s + d, n)) % MOD
                else:
                    for d in range(d_num):
                        result = (result + dfs(nth + 1, s + d, n)) % MOD
                s += d_num
            if min_sum <= s <= max_sum:
                result = (result + 1) % MOD
            return result
        result = count(num2) - count(str(int(num1)-1))
        return (result + MOD) % MOD
            
