class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1):
            return False
        i = 0
        for c in str1:
            if c == str2[i] or ord(c) + 1 == ord(str2[i]) or (c == 'z' and str2[i] == 'a'):
                i += 1
                if i >= len(str2):
                    return True
        return False
