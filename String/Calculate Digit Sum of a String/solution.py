class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = ""
            i = 0
            while i < len(s):
                new_s += str(sum(map(int, s[i:i+k])))
                i += k
            s = new_s
        return s