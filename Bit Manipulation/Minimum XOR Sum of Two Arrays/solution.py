class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        @cache
        def dfs(idx, mask):
            if idx >= n:
                return 0
            result = math.inf
            for i in range(n):
                if (mask >> i) & 1 == 1:
                    continue
                result = min(result, (nums1[idx] ^ nums2[i]) + dfs(idx + 1, mask | (1<<i)))
              
            return result
        return dfs(0, 0)