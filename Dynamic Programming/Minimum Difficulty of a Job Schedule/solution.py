class Solution:
    def minDifficulty(self, diffs: List[int], d: int) -> int:
        n = len(diffs)

        @cache
        def dfs(i, d):
            if i >= n:
                if d == 0:
                    return 0
                return math.inf
            
            if d == 0:
                return math.inf
            
            result = math.inf
            max_diff = 0
            while n-i-1 >= d-1 and i < n:
                max_diff = max(diffs[i], max_diff)
                i += 1
                result = min(result, max_diff + dfs(i, d-1))
            return result

        result = dfs(0, d)
        if result == math.inf:
            return -1
        return result
        
