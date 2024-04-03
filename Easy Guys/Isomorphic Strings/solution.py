class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sm, tm = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            if s[i] not in sm: sm[s[i]] = t[i]
            if t[i] not in tm: tm[t[i]] = s[i]
            if sm[s[i]] != t[i] or tm[t[i]] != s[i]: return False
        return True
