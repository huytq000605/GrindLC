class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most(k):
            j = 0
            result = 0
            for i in range(len(nums)):
                k -= nums[i] % 2
                while k < 0:
                    k += nums[j] % 2
                    j += 1
                result += i - j + 1
            return result
        return at_most(k) - at_most(k-1)
