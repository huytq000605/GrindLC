@cache
def prime_score(num):
    result = 0
    for i in range(2, math.ceil(math.sqrt(num))):
        mark = False
        while num % i == 0:
            mark = True
            num //= i
        if mark: result += 1
    if num > 1: result += 1
    return result

class Solution:
    def maximumScore(self, nums, k): 
        n = len(nums)
        scores = [prime_score(num) for num in nums]
        left_gte = [-1 for i in range(n)]
        right_gt = [n for i in range(n)]
        # O(N)
        stack = []
        for i in range(n):
            while stack and scores[i] > scores[stack[-1]] :
                right_gt[stack.pop()] = i
            stack.append(i)
        
        # O(N)
        stack = []
        for i in reversed(range(n)):
            while stack and scores[i] >= scores[stack[-1]]:
                left_gte[stack.pop()] = i
            stack.append(i)
        
        # O(NlogN)
        nums = sorted([(nums[i], -i) for i in range(n)])
        
        result = 1
        MOD = 10**9 + 7

        # O(N)
        while nums and k:
            value, i = nums.pop()
            i = -i
            left, right = left_gte[i] + 1, right_gt[i] - 1
            times = min(k, (right - i + 1) * (i - left + 1))
            k -= times
            result = (result * pow(value, times, MOD)) % MOD
        
        return result
            
