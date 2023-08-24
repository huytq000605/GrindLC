class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10**9 + 7
        
        @cache
        def dfs(i, mx, tight, prev_digit, leading_zero):
            if i == len(mx):
                return 1
            start = 0
            end = 9
            if not leading_zero:
                start = max(0, prev_digit-1)
                end = min(9, prev_digit + 1)
            if tight:
                end = min(end, int(mx[i]))
            result = 0
            for digit in range(start, end + 1):
                if not leading_zero and digit == prev_digit: continue
                next_tight = tight
                if digit != int(mx[i]):
                    next_tight = False
                next_leading_zero = leading_zero and digit == 0
                result = (result + dfs(i+1, mx, next_tight, digit, next_leading_zero)) % MOD 
            return result
            
        low = str(int(low) - 1)
        result = dfs(0, high, True, 0, True) - dfs(0, low, True, 0, True)
        return (result + MOD) %MOD
