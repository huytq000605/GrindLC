class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        count = 0
        end = -1
        n = len(nums)
        result = 0
        for start in range(n):
            while end + 1 < n and count < k:
                end += 1
                count += nums[end] == mx
            if count == k:
                result += n-end
            else:
                break
            if nums[start] == mx:
                count -= 1
        return result
