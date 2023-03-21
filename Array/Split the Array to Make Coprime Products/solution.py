class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        divisors = defaultdict(int)
        def factorize(num):
            d = 2
            result = []
            while d * d <= num:
                while num % d == 0:
                    result.append(d)
                    num //= d
                d += 1
            if num > 1:
                result.append(num)
            return result
        
        result = 0
        left, right = Counter(), Counter()
        for num in nums:
            for f in factorize(num):
                right[f] += 1
                
        n = len(nums)
        common = 0
        for i in range(n-1):
            num = nums[i]
            for f in factorize(num):
                left[f] += 1
                right[f] -= 1
                # If we see this factor for the first time
                if left[f] == 1:
                    common += 1
                # It's no longer common factor
                if right[f] == 0:
                    common -= 1
     
            if not common:
                return i
        return -1
        
