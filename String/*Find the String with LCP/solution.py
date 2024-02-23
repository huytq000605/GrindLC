class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        c = -1
        n = len(lcp)
        letters = [-1 for _ in range(n)]
        for i in range(n):
            if letters[i] != -1: continue
            c += 1
            if c >= 26:
                return ""
            letters[i] = c
            for j in range(n):
                if lcp[i][j] > 0: 
                    letters[j] = c

        my_lcp = [[0 for j in range(n+1)] for i in range(n+1)]
        for i in reversed(range(n)):
            for j in reversed(range(n)):
                if letters[i] == letters[j]:
                    my_lcp[i][j] = my_lcp[i+1][j+1] + 1

        for i in range(n):
            for j in range(n):
                if my_lcp[i][j] != lcp[i][j]: return ""
        result = "".join(map(chr, [char_code + ord('a') for char_code in letters]))
        return result
                    
