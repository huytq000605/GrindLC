class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        aXorB = 0
        for num in nums:
            aXorB ^= num
        
        lsb = aXorB & (-aXorB)
        a = 0
        for num in nums:
            if num & lsb: a ^= num
        return [a, a^aXorB]
