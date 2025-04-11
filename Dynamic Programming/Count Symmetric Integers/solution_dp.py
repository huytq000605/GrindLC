class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        @cache
        def dfs(i, n, diff, tight, lt):
            if diff < 0: return 0
            if i >= n:
                return 1 if diff == 0 else 0
            lower = 0 if i else 1
            upper = int(lt[i]) + 1 if tight else 10
            result = 0
            for d in range(lower, upper):
                contribute = d if i < n/2 else -d
                result += dfs(i+1, n, diff + contribute, tight and d == int(lt[i]), lt)
            return result

        low, high = str(low-1), str(high)
        r1 = sum([dfs(0, n, 0, n == len(high), high) for n in range(2, len(high)+1, 2)])
        r2 = sum([dfs(0, n, 0, n == len(low), low) for n in range(2, len(low)+1, 2)])
        return r1 - r2 
