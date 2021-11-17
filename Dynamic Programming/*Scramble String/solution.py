class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(None)
        def dfs(s1, s2):
            if s1 == s2: return True
            for i in range(1, len(s1)):
                left1 = s1[:i]
                right1 = s1[i:]
                left2 = s2[:i]
                right2 = s2[i:]
                left1ToRight2 = s1[:len(right2)]
                right1ToLeft2 = s1[len(right2):]
                if dfs(left1, left2) and dfs(right1, right2): return True
                elif dfs(left1ToRight2, right2) and dfs(right1ToLeft2, left2): return True
            return False
    
        return dfs(s1,s2)