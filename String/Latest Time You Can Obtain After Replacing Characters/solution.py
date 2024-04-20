class Solution:
    def findLatestTime(self, s: str) -> str:
        s = list(s)
        if s[0] == '?':
            s[0] = '1' if s[1] == '?' or int(s[1]) <= 1 else '0'
        if s[1] == '?':
            s[1] = '1' if s[0] == '1' else '9'
        s[3] = '5' if s[3] == '?' else s[3]
        s[4] = '9' if s[4] == '?' else s[4]
        return ''.join(s)
