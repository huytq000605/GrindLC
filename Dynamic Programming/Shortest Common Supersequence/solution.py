from functools import cache

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        @cache
        def dfs(idx1, idx2):
            if idx1 >= len(str1) and idx2 >= len(str2):
                return 0
            if idx1 >= len(str1):
                return len(str2) - idx2
            if idx2 >= len(str2):
                return len(str1) - idx1
            
            if str1[idx1] == str2[idx2]:
                return 1 + dfs(idx1 + 1, idx2 + 1)
            else:
                return min(dfs(idx1 + 1, idx2), dfs(idx1, idx2 + 1)) + 1
            
        resultLength = dfs(0, 0)
        result = ""
        
        i = 0
        j = 0
        for k in range(resultLength):
            if i >= len(str1):
                return result + str2[j:]
            if j >= len(str2):
                return result + str1[i:]
            if str1[i] == str2[j]:
                result += str1[i]
                i += 1
                j += 1
            else:
                if dfs(i + 1, j) <= dfs(i, j + 1):
                    result += str1[i]
                    i += 1
                else:
                    result += str2[j]
                    j += 1
            
        return result