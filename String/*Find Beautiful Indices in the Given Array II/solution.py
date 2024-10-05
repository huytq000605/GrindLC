class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        def lps(s):
            n = len(s)
            j = 0
            lps = [0 for _ in range(n)]
            for i in range(1, n):
                while j and s[i] != s[j]:
                    j = lps[j-1]
                if s[i] == s[j]:
                    j += 1
                    lps[i] = j
            return lps

        def kmp(s, p):
            matched = []
            pattern_lps = lps(p)
            j = 0
            for i in range(len(s)):
                while j and s[i] != p[j]:
                    j = pattern_lps[j-1]
                if s[i] == p[j]:
                    if j == len(p) - 1:
                        matched.append(i- len(p) + 1)
                        j = pattern_lps[j]
                    else:
                        j += 1
            return matched
        
        ma = kmp(s, a)
        mb = kmp(s, b)
        j = 0
        result = []
        for i in ma:
            while j < len(mb) and mb[j] < i - k:
                j += 1
            if j < len(mb) and abs(mb[j] - i) <= k:
                result.append(i) 
        return result
        
        

                        
                    
