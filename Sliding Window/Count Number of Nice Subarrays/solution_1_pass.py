class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        j = 0
        first_odd = 0
        odds = 0
        result = 0

        for i in range(len(nums)):
            if nums[i] % 2: odds += 1
            while odds > k:
                odds -= nums[j] % 2
                j += 1
            first_odd = max(first_odd, j)
            while odds == k and nums[first_odd] % 2 == 0:
                first_odd += 1
            if odds == k: 
                result += first_odd - j + 1
        return result
