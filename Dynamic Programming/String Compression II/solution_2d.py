class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        def lc(count):
            if count == 1: return 0
            return len(str(count))
        @cache
        def dfs(i, k):
            if k < 0:
                return math.inf
            if i >= n:
                return 0
            # s[i:j] are grouped into 1
            # take the letters with the most counte and remove the rest
            counter = Counter()
            most = 0
            result = dfs(i+1, k-1)
            for j in range(i, n):
                counter[s[j]] += 1
                most = max(most, counter[s[j]])
                m = j - i + 1
                result = min(result, lc(most) + 1 + dfs(j+1, k - m + most))
            return result
        return dfs(0, k)
