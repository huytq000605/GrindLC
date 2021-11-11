class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @lru_cache(None)
        def dfs(idx1: int, idx2: int):
            if(idx1 >= len(s1) and idx2 >= len(s2)):
                return 0
            if idx1 >= len(s1):
                return sum([ord(s2[i]) for i in range(idx2, len(s2))])
            if idx2 >= len(s2):
                return sum([ord(s1[i]) for i in range(idx1, len(s1))])
            if s1[idx1] == s2[idx2]:
                return dfs(idx1 + 1, idx2 + 1)
            else:
                return min(ord(s1[idx1]) + dfs(idx1 + 1, idx2), ord(s2[idx2]) + dfs(idx1, idx2 + 1))
        return dfs(0, 0)