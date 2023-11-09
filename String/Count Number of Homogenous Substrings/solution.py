class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        result = 0
        cur_c = ""
        cur = 0
        for c in s:
            if c != cur_c:
                cur_c = c
                cur = 0
            cur += 1
            result = (result + cur) % MOD
        return result
