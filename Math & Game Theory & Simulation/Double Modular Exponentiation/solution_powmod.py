class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        def mod_pow(a, b, mod):
            if b == 0:
                return 1
            half = mod_pow(a, b // 2, mod)
            if b % 2 == 0:
                return (half * half) % mod
            return (half * half * a) % mod
        idx = 0
        result = []
        for a, b, c, m in variables:
            if mod_pow(mod_pow(a, b, 10), c, m) == target:
                result.append(idx)
            idx += 1
        return result
