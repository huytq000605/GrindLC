class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        offset = ord('a')
        @cache
        def dfs(i, mask, can_change):     
            if i >= len(s):
                return 1
            bit_count = mask.bit_count()
            bit = ord(s[i]) - offset
            if bit_count == k and (mask >> bit) & 1 == 0:
                return 1 + dfs(i+1, 1 << bit, can_change)
            result = dfs(i+1, mask | (1 << bit), can_change)
            if can_change:
                for c in range(26):
                    if (mask >> c) & 1:
                        continue
                    if bit_count == k:
                        result = max(result, 1 + dfs(i+1, 1 << c, False))
                    else:
                        result = max(result, dfs(i+1, mask | (1 << c), False))
            return result
        return dfs(0, 0, True)
