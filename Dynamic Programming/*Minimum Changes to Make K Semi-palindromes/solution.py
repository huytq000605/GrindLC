class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        factors = defaultdict(lambda: [1])

        for d in range(2, n):
            for l in range(d+d, n+1, d):
                factors[l].append(d)
        
        @cache
        def semi(i, j, d):
            if i >= j: return 0
            result = 0
            for k in range(d): 
                result += s[i + k] != s[j+1-d+k]
            result += semi(i+d, j-d, d)
            return result

        @cache
        def cost(i, j):
            length = j - i + 1
            result = length
            for d in factors[length]:
                result = min(result, semi(i, j, d))
            return result

        @cache
        def dfs(i, k):
            if k == 1:
                return cost(i, n-1)
            result = math.inf
            for j in range(i+2, n):
                if n - j <= 1:
                    break
                result = min(result, dfs(j, k-1) + cost(i, j-1))
            return result
        return dfs(0, k)
