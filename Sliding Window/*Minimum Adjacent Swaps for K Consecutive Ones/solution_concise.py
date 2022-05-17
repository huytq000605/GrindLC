class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        ones = []
        for i in range(len(nums)):
            if nums[i] == 1:
								# Trick for move every number into one place
                ones.append(i - len(ones))
        n = len(ones)
        
        median = k // 2
        left_size = median
        right_size = k - 1 - left_size
        
        left = sum(abs(ones[median] - ones[i]) for i in range(median))
        right = sum(abs(ones[median] - ones[i]) for i in range(median + 1, k))
        result = left + right
        
        for start in range(1, n - k + 1):
            left -= ones[median] - ones[start - 1]
            left += (ones[median + 1] - ones[median]) * left_size
            
            right += ones[start + k - 1] - ones[median + 1]
            right -= (ones[median + 1] - ones[median]) * right_size
            
            median += 1
            result = min(result, left + right)
        
        return result