class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        
        # Actually can just check if nums have a subarray of length 2 have sum >= m
        # for i in range(n-1):
        #     if nums[i] + nums[i+1] >= m:
        #         return True
        # return False
        
        prefix = [0 for _ in range(n+1)]
        for i in range(n):
            if i > 0:
                prefix[i+1] = prefix[i]
            prefix[i+1] += nums[i]
        
        @cache
        def dfs(start, end):
            if start == end:
                return True
            
            if prefix[end+1] - prefix[start] < m:
                return False
            for mid in range(start, end):
                if dfs(start, mid) and dfs(mid + 1, end):
                    return True
            return False
        
        return dfs(0, n-1)
