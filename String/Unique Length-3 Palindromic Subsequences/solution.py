class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = dict()
        last = dict()
        result = 0
        for i, c in enumerate(s):
            if c not in first: first[c] = i
            last[c] = i
        for c in first.keys():
            i, j = first[c], last[c]
            if i < j:
                result += len(set(s[i+1:j]))
        return result
