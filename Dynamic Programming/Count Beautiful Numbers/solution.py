class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        def count(upper_bound: int):
            s = str(upper_bound)
            digits = [int(d) for d in s]
            n = len(digits)

            @cache
            def dfs(i, s, p, tight, started):
                if i == n:
                    if s == 0: return 0
                    return 1 if p % s == 0 else 0
                result = 0
                if not started:
                    result += dfs(i+1, s, p, False, False)
                beginning = 0 if started else 1
                if tight:
                    for d in range(beginning, digits[i] + 1):
                        result += dfs(i+1, s + d, p * d, d == digits[i], True)
                else:
                    for d in range(beginning, 10):
                        result += dfs(i+1, s + d, p * d, False, True)
                return result
            return dfs(0, 0, 1, True, False)
        
        return count(r) - count(l-1)
