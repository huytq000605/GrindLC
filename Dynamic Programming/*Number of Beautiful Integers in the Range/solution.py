class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        @cache
        def dfs(i, mx, tight, remainder, odd, even, leading_zero):
            if i == len(mx):
                if odd == even and remainder == 0:
                    return 1
                return 0
            
            result = 0
            start = 0
            end = 9
            if tight:
                end = min(end, int(mx[i]))
            for digit in range(start, end + 1):
                next_tight = tight and digit == int(mx[i])
                next_remainder = (remainder * 10 + digit) % k
                next_odd = odd 
                next_even = even
                next_leading_zero = leading_zero and digit == 0
                if digit % 2 == 0 and not next_leading_zero:
                    next_even += 1
                elif digit % 2 == 1:
                    next_odd += 1
                result += dfs(i+1, mx, next_tight, next_remainder, next_odd, next_even, next_leading_zero)
            return result
        return dfs(0, str(high), True, 0, 0, 0, True) - dfs(0, str(low-1), True, 0, 0, 0, True)
            
