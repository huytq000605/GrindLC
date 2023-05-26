class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        bits = [0 for _ in range(45)]
        for num in nums:
            bit = 0
            while num:
                bits[bit] += num & 1
                num >>= 1
                bit += 1
        
        result = 0
        for num in nums:     
            ori = num
    
            bit = 0
            while num:
                bits[bit] -= num & 1
                bits[bit + k] += num & 1
                num >>= 1
                bit += 1
                
            res = 0     
            for bit, is_set in enumerate(bits):
                if is_set:
                    res += 1 << bit
            result = max(result, res)
                    
            num = ori
            bit = 0
            while num:
                bits[bit] += num & 1
                bits[bit + k] -= num & 1
                num >>= 1
                bit += 1
            
        return result
