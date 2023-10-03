class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        num_i = 0
        num_ij = 0
        for num in nums:
            result = max(result, num_ij * num)
            num_ij = max(num_ij, num_i - num)
            num_i = max(num_i, num)
        return result
            
