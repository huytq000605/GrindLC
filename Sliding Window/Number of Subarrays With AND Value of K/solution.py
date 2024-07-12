class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:     
        def val(bits, k):
            result = 0
            for bit in range(32):
                if bits[bit] >= k: result |= (1 << bit)
            return result
        
        def at_least(k):
            result = 0
            start = 0
            bits = [0 for _ in range(32)]
            for i in range(len(nums)):
                num, bit = nums[i], 0
                while num:
                    bits[bit] += num & 1
                    num >>= 1
                    bit += 1
                
                while start <= i and val(bits, i - start + 1) < k:
                    num, bit = nums[start], 0
                    while num:
                        bits[bit] -= num & 1
                        num >>= 1
                        bit += 1
                    start += 1
                
                result += (i - start + 1)
            return result

        return at_least(k) - at_least(k+1)
            
                
