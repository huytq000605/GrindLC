class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0 for i in range(n)]
        for i, num in enumerate(nums):
            if i > 0:
                prefix[i] = prefix[i-1]
            prefix[i] += num
            
        min_avg_diff = math.inf
        result = 0
        
        for i in range(n):
            first = prefix[i] // (i+1)
            last = 0
            if i != n-1:
                last = (prefix[-1] - prefix[i]) // (n-i-1)
            avg = abs(first - last)
            if avg < min_avg_diff:
                min_avg_diff = avg
                result = i
        return result