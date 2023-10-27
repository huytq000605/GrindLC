class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        pref = [math.inf for _ in range(n)]
        
        for i in range(n):
            if i > 0:
                pref[i] = pref[i-1]
            pref[i] = min(pref[i], nums[i])
        
        result = math.inf
        suff = math.inf
        for i in range(n-1, 0, -1):
            if nums[i] > suff and nums[i] > pref[i-1]:
                result = min(result, suff + nums[i] + pref[i-1])
            suff = min(suff, nums[i])
        if result == math.inf:
            return -1
        return result
            
            
            
