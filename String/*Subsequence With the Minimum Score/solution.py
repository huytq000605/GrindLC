class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        # Idea: find the longest prefix and suffix of t which is subsequence of s
        
        # finding the longest suffix
        # suffix[j] = k means s[j:] can match t[k+1:]
        suffix = [-1] * n
        j = len(t) - 1
        for i in reversed(range(n)):
            if j >= 0 and s[i] == t[j]:
                j -= 1
            suffix[i] = j
        result = m
        
        # finding the longest prefix combined with suffix, so we can found
        # what is the min & max index among all removed
        j = 0
        for i in range(n):
            # remove from j to suffix[i]
            result = min(result, max(0, suffix[i] - j + 1))
            if j < m and s[i] == t[j]:
                j += 1
        # remove from idx j to m-1
        return min(result, m-j)
        
        
        
