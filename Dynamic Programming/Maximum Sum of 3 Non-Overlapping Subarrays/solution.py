class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        cur = 0
        total = [0 for i in range(n+1-k)]
        for i in range(n):
            cur += nums[i]
            if i >= k-1:
                total[i+1-k] = cur
                cur -= nums[i+1-k]

        @cache
        def dfs(i, m):
            if m == 0:
                return 0
            if i > (n-k):
                return 0
            return max(dfs(i + k, m - 1) + total[i], dfs(i+1, m))
        
        dfs(0, 3)
        i = 0
        m = 3
        result = []
        while i <= n - k and m > 0:
            if total[i] + dfs(i+k, m-1) >= dfs(i+1,m):
                result.append(i)
                m -= 1
                i += k
                continue
            i += 1
                
        return result