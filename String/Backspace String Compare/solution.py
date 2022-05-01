class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        while True:
            back = 0
            while i >= 0 and (back > 0 or s[i] == "#"):
                if s[i] == "#":
                    back += 1
                else:
                    back -= 1
                i -= 1
            
            back = 0
            while j >= 0 and (back > 0 or t[j] == "#"):
                if t[j] == "#":
                    back += 1
                else:
                    back -= 1
                j -= 1
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
                i -= 1
                j -= 1
            else:
                break
        
        return i < 0 and j < 0