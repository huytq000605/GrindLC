class Solution:
    def checkString(self, s: str) -> bool:
        met = False
        for l in s:
            if l == "b":
                met = True
            if met and l == "a":
                return False
        return True
