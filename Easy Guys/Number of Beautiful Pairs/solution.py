class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            for j in range(i+1, n):
                first = int(str(nums[i])[0])
                last = int(str(nums[j])[-1])
                if math.gcd(first, last) == 1:
                    result += 1
                    
        return result
