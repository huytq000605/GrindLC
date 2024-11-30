class Solution:
    def countKReducibleNumbers(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        @cache
        def dfs(i, eq, set_bit):
            if i == len(s):
                if eq: return 0
                t = 1
                num = set_bit
                while num > 1 and t < k:
                    set_bit = 0
                    while num:
                        set_bit += num & 1
                        num >>= 1
                    num = set_bit
                    t += 1
                return num == 1
                # evaluate here
            if not eq:
                return (dfs(i+1, eq, set_bit + 1) + dfs(i+1, eq, set_bit)) % MOD
            result = dfs(i+1, s[i] == '0', set_bit)
            if s[i] == '1':
                result = (result + dfs(i+1, eq, set_bit + 1)) % MOD
            return result
        return dfs(0, True, 0)
                
