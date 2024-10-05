class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        @cache
        def is_possible(i, j, diff):
            if i >= len(s1) and j >= len(s2): return diff == 0
            if i < len(s1) and s1[i].isdigit():
                cur = 0
                while i < len(s1) and s1[i].isdigit():
                    cur = cur * 10 + int(s1[i])
                    i += 1
                    if is_possible(i, j, diff + cur): return True
            elif j < len(s2) and s2[j].isdigit():
                cur = 0
                while j < len(s2) and s2[j].isdigit():
                    cur = cur * 10 + int(s2[j])
                    j += 1
                    if is_possible(i, j, diff - cur): return True
            elif diff == 0:
                if i >= len(s1) or j >= len(s2) or s1[i] != s2[j]: return False
                return is_possible(i+1, j+1, diff)
            elif diff > 0: 
                if j >= len(s2): return False
                return is_possible(i, j+1, diff-1)
            elif diff < 0: 
                if i >= len(s1): return False
                return is_possible(i+1, j, diff+1)

            return False
        
        return is_possible(0, 0, 0)

