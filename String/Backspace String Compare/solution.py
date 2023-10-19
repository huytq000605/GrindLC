class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s)-1, len(t)-1
        bs, bt = 0, 0
        while True:
            while i >= 0:
                if s[i] == "#":
                    bs += 1
                elif bs:
                    bs -= 1
                else:
                    break
                i -= 1
            
            while j >= 0:
                if t[j] == "#":
                    bt += 1
                elif bt:
                    bt -= 1
                else:
                    break
                j -= 1
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
                i -= 1
                j -= 1
            else:
                break
        return i == -1 and j == -1
                
