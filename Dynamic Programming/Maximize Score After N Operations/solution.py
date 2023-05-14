class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(mask):
            set_bit = 0
            for i in range(n):
                if (mask >> i) & 1:
                    set_bit += 1
            
            result = 0
            
            turn = set_bit // 2 + 1
            for i in range(n):
                if (mask >> i) & 1:
                    continue
                for j in range(n):
                    if (mask >> j) & 1 or j == i:
                        continue
                    next_mask = mask | (1 << i) | (1 << j)
                    result = max(result, math.gcd(nums[i], nums[j]) * turn + dfs(next_mask))
            return result
        return dfs(0)
                
