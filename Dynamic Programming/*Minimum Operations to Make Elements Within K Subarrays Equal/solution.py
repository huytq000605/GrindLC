
from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        lower, upper = SortedList(), SortedList()
        sl = 0
        su = 0
        def put(num):
            nonlocal sl, su
            lower.add(num)
            sl += num
            while len(lower) > len(upper) + 1:
                v = lower[-1]
                upper.add(v)
                su += v
                lower.remove(v)
                sl -= v
                
            while len(upper) > len(lower):
                v = upper[0]
                upper.remove(v)
                su -= v
                lower.add(v)
                sl += v
            
            while upper and lower and lower[-1] > upper[0]:
                v1 = lower[-1]
                v2 = upper[0]
                lower.remove(v1)
                upper.remove(v2)
                lower.add(v2)
                upper.add(v1)
                sl += v2 - v1
                su += v1 - v2

        for num in nums[:x]:
            put(num)
        
        # cost[i] = make subarray[i:i+x] equal
        cost = [math.inf for _ in range(n-x+1)]
        cost[0] = lower[-1] * len(lower) - sl + su - lower[-1] * len(upper)
        for i in range(x, n):
            if nums[i-x] in lower:
                lower.remove(nums[i-x])
                sl -= nums[i-x]
            else:
                upper.remove(nums[i-x])
                su -= nums[i-x]
            put(nums[i])
            cost[i-x+1] = lower[-1] * len(lower) - sl + su - lower[-1] * len(upper)

        # dp[i] = min cost with i first elements
        dp = [0 for _ in range(n+1)]
        for i in range(k):
            ndp = [math.inf for _ in range(n+1)]
            for j in range(x, n+1):
                ndp[j] = min(ndp[j-1], dp[j-x] + cost[j-x])
            dp = ndp
        return ndp[-1]
