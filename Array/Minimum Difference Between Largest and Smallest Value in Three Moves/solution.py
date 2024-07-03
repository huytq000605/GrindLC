class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3: return 0
        top4 = []
        btm4 = []
        for num in nums:
            heappush(top4, num)
            heappush(btm4, -num)
            if len(top4) > 4: heappop(top4)
            if len(btm4) > 4: heappop(btm4)
        
        btm4 = sorted([-num for num in btm4])
        return min([num - btm4[i] for i, num in enumerate(sorted(top4))])
