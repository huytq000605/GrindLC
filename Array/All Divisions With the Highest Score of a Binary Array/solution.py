class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        result = []
        cur_score = 0
        n = len(nums)
        ones = 0
        for num in nums:
            if num == 1:
                ones += 1
        
        right_ones = ones
        left_zeros = 0
        
        for i in range(n+1):
            score = left_zeros + right_ones
            if score == cur_score:
                result.append(i)
            elif score > cur_score:
                cur_score = score
                result = [i]
            if i == n:
                break
            if nums[i] == 1:
                right_ones -= 1
            else:
                left_zeros += 1
        
        return result