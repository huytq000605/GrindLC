class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10**9 + 7
        d1, d2 = len(num1), len(num2)
        @cache
        def dfs(ith, s, n):
            # print(ith, s, n)
            if ith >= n:
                if s >= min_sum and s <= max_sum:
                    return 1
                return 0
            result = 0
            for i in range(10):
                result += dfs(ith+1, min(s+i, max_sum+1), n)
                result %= MOD
            return result
        
        result = 0
        for digits in range(d1+1, d2):
            for i in range(1, 10):
                result += dfs(1, i, digits)
                result %= MOD
        # d1 == d2
        if d1 == d2:
            s1, s2 = 0, 0
            eq = True
            for i in range(d1):
                n1, n2 = int(num1[i]), int(num2[i])
                if eq:
                    for d in range(n1+1, n2):
                        result += dfs(i+1, min(s1+d, max_sum+1), d1)
                        result %= MOD
                    if n1 != n2:
                        eq = False
                else:
                    for d in range(int(num1[i]) + 1, 10):
                        result += dfs(i+1, min(s1+d, max_sum+1), d1)
                        result %= MOD
                    for d in range(int(num2[i])):
                        result += dfs(i+1, min(s2+d, max_sum+1), d2)
                        result %= MOD
                s1 += n1
                s2 += n2
            if min_sum <= s1 <= max_sum:
                result += 1
            
            if num1 != num2 and min_sum <= s2 <= max_sum:
                result += 1
            
            return result % MOD
        
        # d == len(num1)
        s = 0
        for i in range(d1):
            for d in range(int(num1[i]) + 1, 10):
                result += dfs(i+1, min(s+d, max_sum+1), d1)
                result %= MOD
            s += int(num1[i])
        if min_sum <= s <= max_sum:
            result += 1
        
        # d == len(num2)
        s = 0
        for i in range(d2):
            if i == 0:
                for d in range(1, int(num2[i])):
                    result += dfs(i+1, min(s+d, max_sum+1), d2)
                    result %= MOD
            else:
                for d in range(int(num2[i])):
                    result += dfs(i+1, min(s+d, max_sum+1), d2)
                    result %= MOD
            s += int(num2[i])
        if min_sum <= s <= max_sum:
            result += 1
            
        return result
            
