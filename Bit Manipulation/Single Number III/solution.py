class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        aXORb = 0
        for num in nums:
            aXORb ^= num
        
        LSB = 0
        for i in range(32):
            if aXORb & (1<<i) != 0:
                LSB = i
                break
        
        a = 0
        for num in nums:
            if num & (1 << i) != 0:
                a ^= num
        
        return [a, a ^ aXORb]