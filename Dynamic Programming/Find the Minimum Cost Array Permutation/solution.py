class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        @cache
        def dfs(prev, mask):
            if mask == (1 << n) - 1:
                return abs(prev - nums[0])
            result = math.inf
            for i in range(n):
                if (mask >> i) & 1: continue
                result = min(result, dfs(i, mask | (1 << i)) + abs(prev - nums[i]))
            return result
        
        # Only the order of the permutation matters
        # We can choose whatever num to start the permutation, here we chose 0
        target = dfs(0, 1)
        result = [0]
        mask = 1
        score = 0
        for _ in range(n-1):
            for i in range(n):
                if (mask >> i) & 1: continue
                if score + abs(result[-1] - nums[i]) + dfs(i, mask | (1 << i)) == target:
                    mask |= (1 << i)
                    score += abs(result[-1] - nums[i])
                    result.append(i)
                    break
        return result
        
            
