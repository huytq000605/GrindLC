class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0
        for i in range(n):
            if nums[i] == k:
                result += 1
            mul = nums[i]
            lcm = nums[i]
            for j in range(i+1, n):
                lcm = (nums[j] * lcm) // math.gcd(nums[j], lcm)
                if lcm == k:
                    result += 1
        return result
