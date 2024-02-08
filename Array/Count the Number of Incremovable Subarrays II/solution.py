class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)

        # start = 0
        left_end = 0
        for end in range(1, n):
            if nums[end] <= nums[left_end]:
                break
            left_end = end
        # the whole array is strictly increasing
        if left_end == n-1:
            return n * (n+1) // 2
        
        # end = n
        # strictly increasing from [right_start, n-1]
        right_start = n-1
        for start in range(n-2, -1, -1):
            if nums[start] >= nums[right_start]:
                break
            right_start = start

        result = 1 # remove everything
        result += left_end + 1
        result += n-1-(right_start)+1
        for left_end in range(left_end+1):
            while right_start < n and nums[right_start] <= nums[left_end]:
                right_start += 1
            result += n-1-right_start+1 # right_start can be [nxt, n-1]
        return result
            
