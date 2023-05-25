class Solution:
    def minLength(self, s: str) -> int:
        while True:
            action = False
            new_s = ""
            i = 0
            while i < len(s):
                if i < len(s) - 1 and s[i:i+2] == "AB" or s[i:i+2] == "CD":
                    i += 2
                    action = True
                else:
                    new_s += s[i]
                    i += 1
            s = new_s
            if not action:
                break
        return len(s)
