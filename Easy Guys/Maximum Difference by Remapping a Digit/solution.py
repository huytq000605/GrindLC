class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        mn = int(s.replace(s[0], "0"))
        first_idx = 0
        for i in range(len(s)):
            if s[i] != "9":
                first_idx = i
                break
        mx = int(s.replace(s[first_idx], "9"))
        return mx - mn
